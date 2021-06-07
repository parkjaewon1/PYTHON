import re
def hexarepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
m = p.sub(hexarepl, 'Call 110 from printing 15 for your code')
print(m)