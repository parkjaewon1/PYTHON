import re # r은 raw String 문자 그 자체
p1 = re.compile(r'\Bclass\B')  # \B는 공란이 없는 것  \b의 반대
p2 = re.compile(r'class')
print(p1.search('no class at all'))
print(p2.search('no class at all'))
print(p1.search('the declassified algorithm'))
print(p2.search('the declassified algorithm'))