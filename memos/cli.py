import click
from click_aliases import ClickAliasedGroup
from memos import __VERSION__
from memos.auth import auth_command
from memos.echo import echo_command
from memos.edit import edit_command
from memos.list import list_command
from memos.new import new_command
from memos.remove import remove_command

@click.group(cls=ClickAliasedGroup)
def cli():
    pass


@click.command(name='version')
def version_command():
    """Prints Memos CLI version"""
    click.echo(f'Memos CLI v{__VERSION__}')


cli.add_command(auth_command)
cli.add_command(echo_command)
cli.add_command(edit_command)
cli.add_command(list_command)
cli.add_command(new_command)
cli.add_command(remove_command)
cli.add_command(version_command)

if __name__ == '__main__':
    cli()
