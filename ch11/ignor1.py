import re
p = re.compile(r'[_a-zA-Z]\w*') # r은 raw
m = p.search('123 abc 123 def') # 전체를 확인하여 조건에 맞는 데이터 한건
print(m.group())
m = p.findall('123 abc 123 def') # 조건에 맞는 데이터 모두
print(m)
p = re.compile('the')
print(p.findall('The cat was hungry, They were scared because of the cat'))
p = re.compile('the', re.I)
print(p.findall('The cat was hungry, They were scared because of the cat'))