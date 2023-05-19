import click
from memos.auth.whoami import whoami_command
from memos.auth.signin import signin_command
from memos.auth.signout import signout_command


@click.group(name='auth')
def auth_command():
    """Manages authentication"""
    pass


auth_command.add_command(signin_command)
auth_command.add_command(whoami_command)
auth_command.add_command(signout_command)
