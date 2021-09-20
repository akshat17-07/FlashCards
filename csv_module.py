import os
import csv

def csv_reader(String_filename):
    try:
        file_size = os.path.getsize(String_filename)
    except OSError:
        return None

    with open(String_filename,newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        file_list = []
        for row in csv_reader:
            if row != []:
                file_list.append(row)
                print(row)
        return file_list

def csv_writer(String_filename, data):
    try:
        file_size = os.path.getsize(String_filename)
        with open(String_filename, 'a') as csv_file:
            writer = csv.writer(csv_file,quoting=csv.QUOTE_ALL)
            writer.writerow(data)

    except OSError:
        with open(String_filename, 'w',newline='') as newfile:
            writer = csv.writer(newfile, quoting=csv.QUOTE_ALL)
            writer.writerow(["Question", "Answer"])
            writer.writerow(data)
