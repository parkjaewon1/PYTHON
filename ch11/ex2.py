import re
p = re.compile("[a-z]+") # 영문자 소문자 1개이상(여러개)
#             012345678
m = p.search("5 python")
print(m.start() + m.end()) # m.start() 첫번째 인덱스  m.end() 마지박 인덱스
# 2 + 8 = 10 인덱스 2번째 부터 8번째 앞에 까지