# re.search(), findall() and match()
import re

s = 'Ming is 27 years old, Ming earns 3500 euro per month.'
d = 'Ming'

# search() returns the first match
res = re.search(r'\d+', s).group()
res_d = re.search(r'[a-zA-Z]', d).group()
print('result of search: ', res)
print('result of search_d: ', res_d)

# findall() returns all matches, without group()
# findall() returns a list
res = re.findall(r'[a-z]', s)
print('result of findall: ', res)  

# 