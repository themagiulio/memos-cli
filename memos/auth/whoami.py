import click
from client.auth import get_me


@click.command(name='whoami')
def whoami_command():
    """Prints the username associated with the current logged in user"""
    user = get_me()
    if user is not None:
        click.echo(user['username'])
    else:
        click.echo('You are not logged in')
