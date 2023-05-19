import click
from client.memo import Memo


@click.command(name='remove')
@click.argument('memo_id')
def remove_command(memo_id):
    """Removes a memo"""
    deleted = Memo().delete(memo_id)
    if not deleted:
        click.echo(f'Cannot remove memo with id {memo_id}', err=True)
        return
    click.echo(f'Removed memo with id {memo_id}')
