import csv
from pprint import pprint

crypto_list = []
with open('crypto-client.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        header = row if index == 0 else header
        temp_dictionary = {header[index]:field for index, field in enumerate(row) if index != 0}
        crypto_list.append(temp_dictionary) if index != 0 else None

pprint(crypto_list)