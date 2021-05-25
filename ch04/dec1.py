from decimal import Decimal
sum = Decimal(0.0) # 정확히 0.0이라는 의미
delta = Decimal("0.1") # 정확히 0.1이라는 의미
for i in range(0, 1000):
    sum += delta
print("합계 :", sum)