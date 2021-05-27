def calculate_change(payment, cost):
    money = payment - cost  # money 거스름돈
    unit = [50000, 10000, 5000, 1000]
    for i in unit:
        print(f"{i}원 지폐 : {money//i}장")
        money %= i
# 테스트
calculate_change(100000, 33000)
print("=============")
calculate_change(500000, 378000)