while True:
    print("구구단 출력할 숫자를 입력하세요")
    num = int(input())
    if num >= 2 and num <= 9:
        print(f"구구단 {num}단")
        for i in range(1, 10):
            print(f"{num} * {i} = {num*i}")
    elif num == 0:
        break
    else:
        print("구구단 숫자가 아니네")