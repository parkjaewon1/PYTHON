# 자리수 합계 367 => 3+6+7 =16, 564=> 5+6+4=> 15
print("정수를 여러자리 입력해 보세요")
num = input()
sum = 0;
for i in range(len(num)):
    sum += int(num[i])
print(sum)
