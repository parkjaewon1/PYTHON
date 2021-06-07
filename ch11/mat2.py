import re
print("글자를 입력 하세요")
num = input() # 숫자를 문자형태로 입력 받겠다는 으미
match1 = re.match('[0-9]',num) # *는 0개 이상
print(match1.group())
match1 = re.match('[0-9]',num)
print(match1)
match1 = re.match('[0-9]+',num) # +는 1개 이상
print(match1)
print(match1.group())
