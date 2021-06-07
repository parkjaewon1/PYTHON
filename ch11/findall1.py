import re
match1 = re.findall('[0-9]',' 1234') # finaall 모든 문자 확인
print(match1)
match1 = re.findall('\s[0-9]',' 1234') # \s 첫글자가 공란이고
print(match1)
match1 = re.match('[0-9]',' 1234') # match는 첫번쨰 글자확인
print(match1)