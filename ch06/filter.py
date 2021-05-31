l1 = [1, -3, 2, 0, -5, 6]
# list안에 값을 각각 대입하여 조건에 맞는 경우에만 list로 저장
print(list(filter(lambda x: x > 0, l1)))
