instr   = 'abcdef'
outstr  = '123456'
# instr에 해당하는 인덱스 문자를 outstr로 변경할 수 있도록 매핑
trans = ''.maketrans(instr, outstr)
str = "hello world"
# str문자를 매핑한대로 변경하라
print(str.translate(trans))