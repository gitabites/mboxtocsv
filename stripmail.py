import csv

writer = csv.writer(open('stripmail.csv', "wb"), quotechar='"', escapechar=' ', quoting=csv.QUOTE_NONE)
reader = csv.reader(open('cleanermail.csv', "rb"), skipinitialspace=True)
writer.writerows(reader)