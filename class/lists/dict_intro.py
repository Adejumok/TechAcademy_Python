d = {}
n = int(input('Enter number of employees: '))
i = 1
while i <= n:
    name = input('Enter Employee Name: ')
    salary = input('Enter Employee Salary: ')
    d[name] = salary
    i = i + 1
for x in d:
    print('the name is: ', x, ' and the salary is: ', d[x])

f={}