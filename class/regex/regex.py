import re

count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('abadadar')
for match in matcher:
    count += 1
    print(match.start(), '...', match.end(), '...', match.group())
    print('Number of occurrence: ', count)
print('next')

matcher = re.finditer('[^a-zA-Z0-9]', 'a7b@k9z')
for match in matcher:
    print(match.start(), '...', match.end(), '...', match.group())
print('next')

matcher = re.finditer('\D', 'a7b@k9z')
for match in matcher:
    print(match.start(), '...', match.end(), '...', match.group())

print('next')
print()
print('Quantifiers: ')
matcher = re.finditer('a*', 'abadada')
for match in matcher:
    print(match.start(), '...', match.end(), '...', match.group())


print('next')
print()
print('Match Method: ')
# In match and full match methods the import has to be a python obj i.e in square brackets
inp = input('Enter: ')
matcher = re.match(inp, 'abcdefgjiju')
if matcher is not None:
    print(matcher.start(), '...', matcher.end(), '...', matcher.group())
else:
    print('Not matched')
