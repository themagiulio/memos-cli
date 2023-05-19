import os
import click
from common.config import get_config_path


@click.command(name='signout')
def signout_command():
    """Sign out from memos"""
    confirm = click.confirm('Are you sure you want to sign out?')
    if confirm:
        os.remove(get_config_path())
