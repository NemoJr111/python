import re
str = 'an apple a day keeps doctor away'
result = re.findall(r'a[\w]*', str)
print(result)