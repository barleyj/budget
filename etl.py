import csv

import dateparser

conversions = {
    'STUMPTOWN': 'STUMPTOWN',
    'STARBUCKS': 'STARBUCKS',
    'MISTOBOX': 'MISTOBOX',
    'DUTCH BROS': 'DUTCH BROTHERS',
    "PEET'S": "PEET'S",
    'FRED M FUEL': 'FRED M FUEL',
    'RON TONKIN': 'RON TONKIN',
    }


def sanitize(description):
    for k in vendor.keys():
        if k in description:
            return k
    else:
#        raise KeyError(description)
        return description.replace('POS DEBIT', '').strip().split('  ')[0]

fast_food = 'Expenses:Food:FastFood'
dining = 'Expenses:Food:Dining'
coffee = 'Expenses:Food:Coffee'
gas = 'Expenses:Car:Gas'

vendor = {
    'STUMPTOWN': {'type': coffee},
    'STARBUCKS': {'type': coffee},
    'MISTOBOX': {'type': coffee},
    'DUTCH BROS': {'type': coffee},
    "PEET'S": {'type': coffee},
    'FRED M FUEL': {'type': gas},
    'RON TONKIN': {'type': 'Expenses:Car:Maintenance'},
    'KAISER': {'type': 'Expenses:Health:Medical'},
    "MCDONALD'S": {'type': fast_food},
    'ITUNES': {'type': 'Expenses:Technology:Storage'},
    'GITHUB': {'type': 'Expenses:Work'},
    'ARCO': {'type': 'Expenses:Car:Gase'},
    'CLATSKANIE PEOPLES': {'type': 'Expenses:Home:Utilities'},
    'FRED MEYER': {'type': 'Expenses:Food:Groceries'},
    'BLIZZARD': {'type': 'Expenses:Entertainment:Games'},
    'MOD PIZZA': {'type': fast_food},
    'OREILLY AUTO': {'type': 'Expenses:Car:Parts'},
    'LOS GORDITOS': {'type': fast_food},
    'MUCHAS GRACIAS': {'type': fast_food},
    'DON PEDROS': {'type': fast_food},
    'Synchrony Bank': {'type': 'Unknown'},
    'AMERICAN EXPRESS': {'type': 'Unknown'},
    'Payment to Chase card': {'type': 'Expenses:CreditCard:Payment'},
    'Online Transfer to CHK': {'type': 'Expenses:Transfer'},
    'Online Transfer to  CHK': {'type': 'Expenses:Transfer'},
    'Online Transfer to SAV': {'type': 'Expenses:Transfer'},
    'Online Transfer to  SAV': {'type': 'Expenses:Transfer'},
    'To FIRST TECH CREDIT UNION': {'type': 'Expenses:Transfer'},
    'TACO BELL': {'type': fast_food},
    'THREE RIVERS': {'type': 'Expenses:Entertainment:MovieTheatre'},
    'SAFEWAY': {'type': 'Expenses:Food:Groceries'},
    'CORNERSTONE': {'type': dining},
    'Online Transfer from CHK': {'type': 'Assets:Transfer'},
    'JIVE SOFTWARE': {'type': 'Assets:Paycheck'},
    'PAYPAL': {'type': 'Unknown'},
    'SIZZLE PIE': {'type': fast_food},
    'CASCADE NETWORKS': {'type': 'Expenses:Technology:Internet'},
    'ROCK BOTTOM': {'type': dining},
    'Wal-Mart': {'type': 'Expenses:Food:Groceries'},
    'CITY OF PORTLAND': {'type': 'Expenses:Car:Parking'},
    'WILCO': {'type': 'Expenses:Animals:Food'},
    'CHEVRON': {'type': gas},
    'BURGERVILLE': {'type': fast_food},
    'MICROSOFT': {'type': 'Expenses:Technology:Computer'},
    'NATIONSTAR': {'type': 'Expenses:Home:Mortgage'},
    'E-SAN': {'type': fast_food},
    'CASA BLANCA': {'type': fast_food},
    'BURGER KING': {'type': fast_food},
    'DISCOVER': {'type': 'Expenses:CreditCard:Payment'},
    'SIMPLE': {'type': 'Expenses:Transfer'},
    "KENNY & ZUKE'S": {'type': dining},
    'Amazon Video': {'type': 'Expenses:Entertainment:Television'},
    "PAPA MURPHY'S": {'type': fast_food},
    "WENDYS": {'type': fast_food},
    'STIA PUBLIC PARKING': {'type': 'Expenses:Travel:Parking'},
    'PEETS': {'type': coffee},
    'UBER': {'type': 'Expenses:Travel:Taxi'},
    "PANCHITA'S": {'type': fast_food},
    "OGAWASHI": {'type': dining},
    "KOJACK'S": {'type': dining},
    "MISSION BEACH SURF": {'type': 'Expenses:Misc'},
    'SANDBAR GRILL': {'type': dining},
    'MARRIOTT GASLAMP': {'type': 'Expenses:Travel:Hotel'},
    'DNCSS SAN DIEGO': {'type': fast_food},
    'SOVEREIGN': {'type': dining},
    'PILOT': {'type': gas},
    'BOMBAY CHAAT': {'type': fast_food},
    }


def lookup(description):
    return vendor.get(description, {'type': 'Expenses'})


def process(detail, posted, description, amount, transaction_type, *args):
    return {
        'detail': detail.lower(),
        'posted': dateparser.parse(posted),
        'description': sanitize(description),
        'amount': float(amount),
    }


def print_ledger(posted, description, amount, **args):
    header = '{} * {}'.format(posted.strftime('%Y-%m-%d'), description)
    record = '  {0:<40}$ {1:.2f}'.format(
        lookup(description)['type'],
        amount)
    balance = '  {0:<40}$ {1:.2f}'.format(
        'Assets:Checking',
        amount*-1)
    print(header)
    print(record)
    print(balance)


#print('C 1h = $54')
#print('C 1m = $0.90')
#print('')

with open('FILENAME.CSV') as statement:
    statement_reader = csv.reader(statement)
    for trans in list(statement_reader)[1:]:
        transaction = process(*trans)
        print_ledger(**transaction)
