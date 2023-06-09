import click

common_options = [
    click.option(
        "--debug",
        default=False,
        is_flag=True,
        help="Enables debug mode",
    ),
    click.option(
        "--dry-run",
        default=False,
        is_flag=True,
        help="Enables dry run mode",
    ),
    click.option(
        "-v",
        "--verbose",
        default=False,
        count=True,
        help="Enables verbose mode",
    ),
]
