import os
import tempfile
from io import FileIO
from subprocess import call
import click
from client.memo import Memo
from common.config import read_config


@click.command(name='new')
def new_command():
    """Creates a new memo"""
    f_hnd, f_name = tempfile.mkstemp(suffix='.memos.tmp')
    f_obj = FileIO(f_hnd, 'w')
    f_obj.close()

    editor = read_config('text-editor') or 'vi'

    call(f'{editor} {f_name}'.split(' ')) 

    content = ''

    with open(f_name, 'r', encoding='utf-8') as f_obj:
        content = f_obj.read().rstrip()

    os.remove(f_name)

    memo = Memo().post({'content': content})

    if memo is None:
        click.echo('Cannot create memo', err=True)
        return

    memo_id = memo['id']

    click.echo(f'Created memo with id {memo_id}')
