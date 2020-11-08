import json
from pprint import pprint

import click


@click.group()
def cli():
     pass

@click.command()
@click.option('-s', '--seller', help='seller name')
@click.argument('source', type=click.File('rt', encoding='utf8'))
def search(seller, source):
    for receipt_data in json.load(source):
        ticket = receipt_data['ticket']
        document = ticket['document']
        receipt = document.get('receipt', None)
        if seller.upper() in receipt.get('user', '').upper():
            pprint(receipt)

cli.add_command(search)

if __name__ == '__main__':
    cli()