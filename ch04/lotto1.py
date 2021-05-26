from random import randint
number = []
print('몇개를 지정된 번호로 할래')
num = int(input())
while len(number) < num:
    print('어떤 수로 하고 싶은데')
    num1 = int(input())
    if num1 not in number:
        number.append(num1)
while len(number) < 6:
    ran = randint(1, 45)  # 1부터 45사이 정수
    if ran not in number: # 발생한 숫자가 number에 없으면
        number.append(ran)
print(sorted(number))