import csv
with open("emp.csv", "w",  newline="") as f:
    w=csv.writer(f)
    w.writerow(["EMP NO", "EMP NAME", "EMP SAL", "EMP ADDR"])
    n=int(input("Enter Number of Employees: "))
    for i in range(n):
        no=input("Enter Employee No: ")
        name=input("Enter Employee Name: ")
        sal=input("Enter Employee Salary: ")
        addr=input("Enter Employee Address: ")
        w.writerow([no, name, sal, addr])
print("Total Employees data written to csv successfully!")
