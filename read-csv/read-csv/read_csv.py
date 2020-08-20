import random

def write_random_csv():
    with open("myfile.csv", "w") as f:
        for i in range(6):
            r = random.randrange(100)
            f.write(f'{r},')

write_random_csv()
