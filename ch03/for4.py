# 주사위를 두번 던져서 합이 4의 배수인 경우를 출력하시오
for i in range(1, 7): # 첫 번째 1 ~ 6
    for j in range(1, 7):
        k = i + j
        if k %4 == 0:
            print(f"{i} + {j} = {i+j}")