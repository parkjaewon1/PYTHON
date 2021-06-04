file = open('chicken.txt', 'r', encoding='utf-8')
sum = 0
for i in file:
    data = i.strip().split(": ")
    print("날짜:", data[0], "매출액: ", data[1])  # 날짜, 금액
    sum += int(data[1])
    print(f"매출금액 합계: {sum}")
    file.close()
