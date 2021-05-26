l1 = [2, 7, 3, 6]
# l1.sort() : l1의 원본 데이터가 변경
l2 = sorted(l1)  # 원본 데이터는 변경되지 않고 정열된 결과를 l2에 저장
print('원본',l1)
print('오름차순 :',l2)
l3 = sorted(l1, reverse=True) # 원본 데이터는 변경되지 않고 내림차순으로 변경된 결과를 l3에 저장
print('원본',l1)
print('내림차순 :',l3)
# l1.reverse() 원본 데이터의 저장순서가 거꾸로 된다
l1.sort(reverse=True) # 원본 데이터를 내림차순으로 변경
print('원본변경 :',l1)