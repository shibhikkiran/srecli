# -*- config: utf-8 -*-
"""
cli.py

This module contains basic wrapper to initliaize CLI object.
"""

##
import os
import sys
import platform
import traceback

##
import click
from loguru import logger

##
from srecli.options.common import common_options

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


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


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
        try:
            mod = __import__(
                "srecli.commands.cmd_" + name,
                None,
                None,
                ["cli"],
            )
        except ImportError as err:
            print(err)
            return
        current_os = platform.system()
        if hasattr(mod, "SUPPORT_OS"):
            if (
                current_os.lower()
                not in mod.SUPPORT_OS
            ):
                if SreCLI.list_commands_executed:
                    return None
                else:
                    ctx.fail(
                        f"This command {name} only support to be run on {','.join(mod.SUPPORT_OS)}"
                    )
        else:
            ctx.fail(
                f"SUPPORT_OS is not defined for your command {name} module."
            )

        return mod.cli


@add_options(common_options)
@click.command(
    cls=SreCLI, context_settings=CONTEXT_SETTINGS
)
@pass_context
def cli(ctx, debug, dry_run, verbose):
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
