# -*- config: utf-8 -*-
"""
cmd_status.py

This module contains all subcommands for status command group.
"""

import click

##
from srecli.cli import pass_context, add_options
from srecli.options.common import common_options

# This var should be added to every command module i.e cmd_xxx.py
SUPPORT_OS = ["linux"]


@click.group()
def cli():
    """
    Returns status command group.
    """
    pass


@add_options(common_options)
@cli.command(short_help="Show status")
@click.option(
    "--echo-msg",
    default="Hello",
    help="Message to echo",
)
@pass_context
def show(ctx, debug, dry_run, verbose, echo_msg):
    """
    Returns show command.
    """
    if debug:
        click.echo(
            f"command option passed: --debug={debug}, --dry-run={dry_run}, --verbose={verbose}"
        )
    ctx.logger.debug("This is debug msg")
    ctx.logger.info("This is info msg")
    ctx.logger.warning("This is warning msg")
    ctx.logger.error("This is error msg")
    ctx.logger.critical("This is critical msg")
    ctx.logger.success("This is success msg")
    click.echo(f"echo msg: {echo_msg}")
