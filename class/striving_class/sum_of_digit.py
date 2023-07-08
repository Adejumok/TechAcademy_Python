digit = [123, 456, 789]
sum = 0
for num in digit:
    for n in str(num):
        sum += int(n)
print(sum)