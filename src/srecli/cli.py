# -*- config: utf-8 -*-
"""
cli.py

This module contains basic wrapper to initliaize CLI object.
"""

##
import os
import sys
import traceback

##
import click
from loguru import logger


FORMATTER = "{time:YYYY/MM/DD HH:mm:ss zz!UTC} | {level: <8} | {message}"
FORMATTER_DEBUG = "{time:YYYY/MM/DD HH:mm:ss zz!UTC} | {level: <8} | {name}.{function}:{line} | PID={process} | {message}"

debug_mode = "--debug" in sys.argv

if debug_mode:
    logger.remove(0)
    logger.add(
        sys.stderr,
        format=FORMATTER_DEBUG,
        level="DEBUG",
        colorize=True,
    )
else:
    logger.remove(0)
    logger.add(
        sys.stderr,
        format=FORMATTER,
        level="INFO",
        colorize=True,
    )


CONTEXT_SETTINGS = dict(
    auto_envvar_prefix="SRECLI"
)


class Context:
    """
    A class for setting context variables for CLI.
    """

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.logger = logger


pass_context = click.make_pass_decorator(
    Context, ensure=True
)
base_folder = os.path.dirname(__file__)
cmd_folder = os.path.join(base_folder, "commands")


class SreCLI(click.MultiCommand):
    """
    A class to initialize CLI tool with all its subcommands and help messages.
    """

    list_commands_executed = False

    def list_commands(self, ctx):
        """
        Returns list of commands.
        """
        pass
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(
                ".py"
            ) and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        SreCLI.list_commands_executed = True
        return rv

    def get_command(self, ctx, name):
        """
        Gets a specific command given.
        """
        mod = __import__(
            "srecli.commands.cmd_" + name,
            None,
            None,
            ["cli"],
        )
        return mod.cli


@click.command(
    cls=SreCLI, context_settings=CONTEXT_SETTINGS
)
@click.option(
    "--debug",
    is_flag=True,
    default=False,
    help="Enables debug mode",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Enables dry run mode",
)
@pass_context
def cli(ctx, debug, dry_run):
    """
    Return CLI object.
    """
    pass


if __name__ == "__main__":
    try:
        cli()
    except Exception as err:
        exit_code = 1
        if hasattr(err, "exit_code"):
            exit_code = err.exit_code
        print(f"{traceback.format_exc()}")
        sys.exit(exit_code)
