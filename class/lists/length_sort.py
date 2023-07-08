num = int(input('Enter the number of arguments: '))
n = 0
args=[]
while n < num:
    args.append(input('Enter the string: '))
    n += 1
args.sort(key=len)

print(args)
