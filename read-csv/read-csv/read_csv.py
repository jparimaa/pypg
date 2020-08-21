import random
import csv

def write_random_csv(path):
    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for i in range(5):
            values = []
            for j in range(5):
                values.append(str(random.randrange(100)))
            csv_writer.writerow(values)

def read_csv(path):
    with open(path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        values = []
        for row in csv_reader:
            values += row
        return values

path = 'myfile.csv'
write_random_csv(path)
values = read_csv(path)
print(max(values))
