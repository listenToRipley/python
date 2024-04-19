import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comment_qty'])
    writer.writerow([555, 'ripley', 666])
    writer.writerow([444, 'author', 42])
    