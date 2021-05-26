# 자리수 합계 367 => 3+6+7 =16, 564=> 5+6+4=> 15
print("정수를 여러자리 입력해 보세요")
num = int(input()) # 정수로 처리
sum = 0
while num != 0:
    sum += num % 10 # 0+7 => 7+6 => 13 + 3
    num = num // 10 # 36  => 3  => 0
print(sum)