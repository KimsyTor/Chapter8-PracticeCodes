import csv
from pprint import pprint

with open('crypto-client.csv', 'r') as file:
    reader = csv.DictReader(file)
    crypto_list = [row for row in reader]

pprint(crypto_list)