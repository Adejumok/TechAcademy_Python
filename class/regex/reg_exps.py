import re
s = input('Enter mail: ')
m=re.fullmatch('\w[a-zA-z0-9_.]*@gmail[.]com',s)