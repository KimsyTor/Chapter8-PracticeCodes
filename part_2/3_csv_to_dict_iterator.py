import csv
from pprint import pprint

with open('crypto-client.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    crypto_list = [{header[index]:field for index, field in enumerate(row) if index != 0} for row in reader]

pprint(crypto_list)