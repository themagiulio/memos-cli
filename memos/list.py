import click
from prettytable import PrettyTable
from client.memo import Memo


@click.command(name='list')
@click.option('-p', '--public', is_flag=True, default=False, help='Show public memos')
def list_command(public):
    """Lists memos"""
    model = Memo()
    if public:
        memos = model.get('all')
    else:
        memos = model.get('')
    if memos is None:
        click.echo('Cannot fetch memos', err=True)
    else:
        t = PrettyTable()
        t.align = 'l'
        t.field_names = ['#', 'CREATOR', 'CONTENT']
        for memo in memos:
            content = memo['content'].split()[:5]
            content = ' '.join(content) + '...'
            t.add_row([memo['id'], memo['creatorName'], content])

        print(t)
