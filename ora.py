import json
from pprint import pprint
from datetime import datetime

import click


@click.group()
def cli():
     pass

@click.command()
@click.option('-s', '--seller', help='seller''s name')
@click.option('-d', '--date', 'search_date_str', help='receipt date (selling date)')
@click.option('-e', '--email', help='seller''s email address')
@click.option('-i', '--inn', help='seller''s INN')
@click.argument('source', type=click.File('rt', encoding='utf8'))
def search(seller, search_date_str, email, inn, source):
    for receipt_data in json.load(source):
        ticket = receipt_data['ticket']
        document = ticket['document']
        receipt = document.get('receipt', None)

        if seller and seller.upper() in receipt.get('user', '').upper():
        if not receipt:
            continue
            pprint(receipt)

        if search_date_str:
            search_date = datetime.fromisoformat(search_date_str).date()
            receipt_date = datetime.fromisoformat(receipt['dateTime']).date()
            if receipt_date == search_date:
                pprint(receipt)

        if email and email.upper() in receipt.get('sellerAddress', '').upper():
            pprint(receipt)

        if inn and inn in receipt.get('userInn', ''):
            pprint(receipt)


cli.add_command(search)

if __name__ == '__main__':
    cli()