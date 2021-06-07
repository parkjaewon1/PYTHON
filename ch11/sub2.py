import re
p = re.compile(r'(?P<name>\w+)\s+(?P<tel>\d+[-]\d+[-]\d+)')
# \g는 group의 약자
m = p.sub('\g<tel> \g<name>', 'park 010-1234-5678')
print(m)
p2 = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m2 = p2.sub('\g<2> \g<1>', 'park 010-1234-5678')
print(m2)