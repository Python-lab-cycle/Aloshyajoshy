import csv
with open('employee.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("empno employ name")
    print("--------------------")
    for row in data:
        print(row['empno'],row['employ name'])
