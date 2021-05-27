from random import randint
lotto = set()
while len(lotto) < 6:
    ran = randint(1, 45) # 1 ~ 45사이의 정수 random하게 발생
    lotto.add(ran)
print("로토번호 : ",sorted(lotto))