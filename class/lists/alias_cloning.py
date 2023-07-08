#alias
x=[10, 20, 30]
y=x
print(y)
print(x)
print(id(x))
print(id(y))
x[0]=0
print(y)
print(x)
print(id(x))
print(id(y))
print()

#cloning using slicing operator
x=[10, 20, 30]
y=x[:]
print(y)
print(x)
print(id(x))
print(id(y))
x[0]=0
print(y)
print(x)
print(id(x))
print(id(y))

#using copy
x=[10, 20, 30]
y=x.copy()
print(y)
print(x)
print(id(x))
print(id(y))
x[0]=0
print(y)
print(x)
print(id(x))
print(id(y))