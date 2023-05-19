import os
import tempfile
from subprocess import call
from io import FileIO
import click
from client.memo import Memo


@click.command(name='edit')
@click.argument('memo_id')
def edit_command(memo_id):
    """Edit a memo"""
    memo = Memo().get(memo_id)

    if memo is None:
        click.echo(f'Cannot fetch memo with id {memo_id}', err=True)
        return

    content = memo['content']

    f_hnd, f_name = tempfile.mkstemp(suffix='.memos.tmp')
    f_obj = FileIO(f_hnd, 'w')
    f_obj.write(bytes(content, encoding='utf-8'))
    f_obj.close()

    call(f'vi {f_name}'.split(' ')) 

    updated_content = content

    with open(f_name, 'r', encoding='utf-8') as f_obj:
        updated_content = f_obj.read()

    os.remove(f_name)

    updated = Memo().patch(memo_id, {'content': updated_content})

    if not updated:
        click.echo(f'Cannot update memo with id {memo_id}', err=True)
