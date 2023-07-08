import re

inp = input('Enter: ')
matcher = re.search(inp, 'abcdefgjiju')
if matcher is not None:
    print(matcher.start(), '...', matcher.end(), '...', matcher.group())
else:
    print('Not matched')


l=re.findall('[0-9]', 'a7b9c5kz')
print(l)
print(type(l))


l=re.sub('[0-9]','$', 'a7b9c5kz')
print(l)
print(type(l))
print()

l1=re.subn('[a-z]','@', 'a7b9c5kz')
print(l1)
print(type(l1))
print('Result string: ', l1[0])
print('Replacement numbers: ', l1[1])