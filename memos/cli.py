import click
from click_aliases import ClickAliasedGroup
from memos.auth import auth_command
from memos.echo import echo_command
from memos.edit import edit_command
from memos.list import list_command
from memos.new import new_command


@click.group(cls=ClickAliasedGroup)
def cli():
    pass

cli.add_command(auth_command)
cli.add_command(echo_command)
cli.add_command(edit_command)
cli.add_command(list_command)
cli.add_command(new_command)

if __name__ == '__main__':
    cli()
