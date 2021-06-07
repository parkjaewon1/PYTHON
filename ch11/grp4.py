import re
p = re.compile(r'(\b\w+)\s+\1') # \1은 group(1)이 반복
m = p.search('Paris is the the spring')
print(m.group())