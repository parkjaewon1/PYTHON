import re
#  \w단어 여러개 \d+ 숫자 여러게 \s 공란
p1 = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p1.match('park 010-1234-1234')
print(m)
print(m.group())
# 0은 전체, 1은 첫번째 park, 2는 전화번호 전체 괄호, 3은 010, 4는 마지막 숫자

p2 = re.compile(r'(\w+)+\s+((\d+)+[-]\d+[-](\d+))+')
m = p2.match('park 010-1234-1234')
print(m.group(0)) # 조건에 맞는 것을 전체 출력
print(m.group(1)) # 조건에 맞는 첫번째 그룹
print(m.group(2)) #    "      2
print(m.group(3))
print(m.group(4))
print(m.group(2)+" "+m.group(1))
