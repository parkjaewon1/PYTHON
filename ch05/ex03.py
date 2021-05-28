input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
# 입력된 값은 문자로 인식한다
total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
# 정수로 변경한 후에 연산해야 된다
total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)