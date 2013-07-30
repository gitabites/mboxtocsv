import csv
file_read = csv.DictReader(open('dated_mail.csv', 'rb'), ['subject', 'from', 'date'])
file_write = csv.DictWriter(open('final_mail.csv', 'wb'), ['subject', 'from', 'date'])
file_write.writeheader()
file_write.writerows(file_read)
