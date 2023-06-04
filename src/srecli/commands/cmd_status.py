# -*- config: utf-8 -*-
"""
cmd_status.py

This module contains all subcommands for status command group.
"""

import os
import time
import click


from srecli.cli import pass_context


@click.group()
def cli():
    """
    Returns status command group.
    """
    pass


@cli.command(short_help="Show status")
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
@click.option(
    "--echo-msg",
    default="Hello",
    help="Message to echo",
)
@pass_context
def show(ctx, debug, dry_run, echo_msg):
    """
    Returns show command.
    """
    ctx.logger.debug("This is debug msg")
    ctx.logger.info("This is info msg")
    ctx.logger.warning("This is warning msg")
    ctx.logger.error("This is error msg")
    ctx.logger.critical("This is critical msg")
    ctx.logger.success("This is success msg")
    click.echo(f"echo msg: {echo_msg}")
