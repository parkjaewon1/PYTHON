import re
p = re.compile('(blue|white|red)')
# sub은 변경, subn은 변경된 갯수를 튜플로 반환
m = p.subn('color', 'blue socks and red shoes and white hat')
print(m)
m2 = p.sub('color', 'blue socks and red shoes and white hat')
print(m2)