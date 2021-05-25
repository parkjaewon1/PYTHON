print("구구단 출력할 숫자를 입력하세요")
num = int(input())
if num >= 2 and num <= 9:
    print(f"구구단 {num}단")
    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")
else:
    print("구간 숫자가 아니네")