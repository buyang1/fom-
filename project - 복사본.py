import csv

f = open("C:/Users/datco/Desktop/fom 미니 프로젝트/train.csv", "r")
reader = csv.reader(f)

for row in reader:
    print(row)