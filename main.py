import csv


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_obj = open('items.csv', 'r')
    reader = csv.reader(file_obj)
    for item in reader:
        print(item)


