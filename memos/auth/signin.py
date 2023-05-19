import click
from client.auth import signin


@click.command(name='signin')
def signin_command():
    """Sign in to memos"""
    host = click.prompt('Server url')
    username = click.prompt('Username')
    password = click.prompt('Password', hide_input=True)
    user = signin(host, username, password)
    if user is not None:
        click.echo(f'Welcome {username}!')
    else:
        click.echo('Invalid username or password')
