import click
from prettytable import PrettyTable
from client.memo import Memo


@click.command(name='list')
@click.option('-p', '--public', is_flag=True, default=False, help='Show public memos')
@click.option('-t', '--tag', type=str, required=False, help='Filter by tag name')
def list_command(public, tag=None):
    """Lists memos"""
    model = Memo()
    query = ''
    params = {}

    if public:
        query = 'all'

    if tag is not None:
        params['tag'] = tag

    memos = model.get(query, params)
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

        if len(memos) > 0:
            click.echo(t)
        else:
            click.echo('Cannot find any memo')
