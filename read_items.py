import csv


class ReadItems:
    def __init__(self, filename, method='r'):
        self.file_obj = open(filename, method)

    def __enter__(self):
        reader = csv.reader(self.file_obj)
        dict_list = []
        header = []
        for row in reader:
            if header:
                dict_list.append(dict(zip(header, row)))
            else:
                header = row
        return dict_list

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)


show_items('items.csv')
