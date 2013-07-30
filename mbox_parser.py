import mailbox
import csv

writer = csv.writer(open("clean_mail.csv", "wb"))
for message in mailbox.mbox('your_mbox_name'):
	writer.writerow([message['subject'], message['from'], message['date']])
