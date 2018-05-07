import csv
from collections import defaultdict
from pprint import pprint

columns = defaultdict(list) # each value in each column is appended to a list

with open('classified.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

pprint(columns['website'])


res = columns['website']
csvfile = "urls.csv"


# Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        v = val.split('www.')
        v1 = v[-1]
        writer.writerow([v1])

