import re
# p = re.compile('a[.]{3,}') # 점 3자이상
p = re.compile('a.{3,}') # \n을 제외한 모든 글자 3개 이상
print(p.match('acccb'))
print(p.match('a....b'))
print(p.match('aaab'))
print(p.match('a.cccb'))