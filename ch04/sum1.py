sum = 0
for i in range(0, 1000):
    sum += 1
print("합계 :",sum)
# sum을 실수로 정의하고 실수를 더하면 0.1이 정확하지 않다
sum = 0.0
for i in range(0, 1000):
    sum += 0.1 # 정획한 0.1인지 모름
print("합계 :",sum)