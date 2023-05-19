import click
from client.memo import Memo


@click.command(name='echo')
@click.argument('memo_id')
def echo_command(memo_id):
    """Prints the content of a memo"""
    memo = Memo().get(memo_id)
    if memo is None:
        click.echo(f'Cannot fetch memo with id {memo_id}', err=True)
        return
    click.echo(memo['content'])
