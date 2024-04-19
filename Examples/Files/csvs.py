import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';') # if not passed the default is a comma.
    writer.writerow(['user_id', 'user_name', 'comment_qty'])
    writer.writerow([555, 'ripley', 666])
    writer.writerow([444, 'author', 42])
    

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';') #what is is set to, in order to reset to a comma.
    print(reader)
    print(type(reader))
    # for line in reader: # gets each row line
    #     print(line)
    for index, line in enumerate(reader):
        print(index, line)
        if index == 0:
            header = line 
            for idx, value in enumerate(line): # display the key value pairs pretty much
                print(f"{header[idx]}: {value}")
        