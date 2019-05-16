# =============== 1
import csv
import random
from pathlib import Path

print('ZAVDANYA 1')
ALPHA = [random.randint(1, 200) for i in range(0, 150)]
BETA = sorted(ALPHA, reverse=True)[:15]
with open('task1.txt', 'w') as f:
    [f.write("%s\n" % item) for item in BETA]
print(BETA)

# =============== 2
print('ZAVDANYA 2')


class Person:
    def __init__(self, name):
        self.name = name
        self.id = id(self)


class WorkerMonth(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = float(salary)

    def out(self):
        print(self.id, self.name, self.salary)


class WorkerHour(Person):
    def __init__(self, name, hour_salary):
        Person.__init__(self, name)
        self.hour_salary = float(hour_salary)
        self.salary = 20.8 * 8 * self.hour_salary

    def out(self):
        print(self.id, self.name, self.salary)


a = WorkerMonth('Vova', 100)
b = WorkerMonth('Dosha', 100)
c = WorkerMonth('Timur', 9999)
z = WorkerMonth('Zzzz', 100)
q = WorkerHour('Makuha', 328)
j = WorkerHour('HHHH', 3)

WORKERS = [z, b, c, a, q, j]
# import pdb
# pdb.set_trace()
# a)
print('a)')
WORKERS.sort(key=lambda x: (-x.salary, x.name))
[i.out() for i in WORKERS]
# b)
print('b)')
[i.out() for i in WORKERS[:5]]
# c)
print('c)')
[print(i.id) for i in WORKERS[-3:]]
# d)
print('d)')
TUPLE = [(item.id, item.name, item.salary)for item in WORKERS]
READ_TUPLE = []
with open('task2.csv', 'w') as f:
    csv_out = csv.writer(f)
    csv_out.writerow(['id', 'name', 'salary'])
    for row in TUPLE:
        csv_out.writerow(row)
with open('task3.csv', newline='') as f:
    csv_in = csv.reader(f, delimiter=',')
    f.readline()
    for row in csv_in:
        if row[3] == 'hour':
            READ_TUPLE.append(WorkerHour(row[1], row[2]))
        else:
            READ_TUPLE.append(WorkerMonth(row[1], row[2]))
# print(*READ_TUPLE)
[i.out() for i in READ_TUPLE]
# e)




# Zavdanya 3
print("ZAVDANYA 3")
NUMBER = random.randint(0, 100)
print("Input number or 'quit' to exit")
minrg = 0
maxrg = 100
Your_num = input()
while Your_num != 'quit':
    try:
        if int(Your_num) in range(0, 100):
            if int(Your_num) > NUMBER:
                if int(Your_num) < maxrg:
                    maxrg = int(Your_num)
                print(f"Answer Меньше try in range [{minrg};{maxrg}]")
                Your_num = input()
                continue
            elif int(Your_num) < NUMBER:
                if int(Your_num) > minrg:
                    minrg = int(Your_num)
                print(f"Answer Больше try in range [{minrg};{maxrg}]")
                Your_num = input()
                continue
            elif int(Your_num) == NUMBER:
                print("Molodets")
                break
        else:
            print(f"Input number in range [{minrg};{maxrg}]")
            Your_num = input()
    except ValueError:
        print("Input INTEGER(Number)")
        Your_num = input()
# Zavdanya 4
print("ZAVDANYA 4")
file = list(Path('data').glob('*.txt'))
for i in file:
    text = i.open(encoding='utf-8').readlines()
print(''.join(sorted(''.join(text).replace('\n', ''), key=lambda s: s.lower())))
# Zavdanya 5
print("ZAVDANYA 5")
print(input("Input text:")[::-1])

