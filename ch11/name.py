import re
p1 = re.compile(r'(\w+)\s+(\d+[-]+\d+[-]+\d+)')
m = p1.search('park 010-1234-5678')
print(m.group(1))
# 괄호가 많은 경우에는 ?P<이름>으로 만들면 그룹명 사용 가능
p2 = re.compile(r'(?P<name>\w+)\s+((?P<kuk>\d+)[-]+\d+[-]+\d+)')
m = p2.search('park 010-1234-5678')
print(m.group("name"))
print(m.group("kuk"))