value = int(input('Enter a binary number: '))
c_counter=0
d_accumulator=0
for i in range(1, value+1):
    d_accumulator += 2 ** c_counter * i
    c_counter += 1
print(d_accumulator)