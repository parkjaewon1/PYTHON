num = 1
while num != 0:
    print('구구단 사용할 숫자를 입력하세요')
    num = int(input())
    if num >= 2 and num <= 9:
        i = 1
        while i <= 9:
            print(f"{num} * {i} = {num*i}")
            i += 1
    else:
        print("구구단 숫자가 아닙니다")
print("프로그램 종료")