'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''

import csv
from pprint import pprint

crypto_list = []
header = []
with open('crypto-client.csv', 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        row_to_dict = {}
        if index == 0:
            header = row
        else:
            for index, field in enumerate(row):
                row_to_dict[header[index]] = field

            crypto_list.append(row_to_dict)

pprint(crypto_list)