import re
p = re.compile('(ABC)+') # ABC그룹으로 묶여서 사용
m = p.match('ABCABCABCAABB OK CC')
print(m)
print(m.group())