import re
p1 = re.compile(r'\bclass\b')  # \b는 공란
p2 = re.compile(r'class')
print(p1.search('no class at all'))
print(p2.search('no class at all'))
print(p1.search('the declassified algorithm'))
print(p2.search('the declassified algorithm'))