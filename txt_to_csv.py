import csv

with open('result_file_backup.txt', 'r', encoding='latin-1') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('resultss.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('company', 'website'))
        writer.writerows(lines)
