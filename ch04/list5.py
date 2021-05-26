# range이용하여 list생성 4앞까지
l1 = list(range(4))
print(l1)
del l1[::2] # 짝수번째 데이터 삭제
print(l1)
l1[1:1] = [2] # 인덱스 1번쨰에 2를 추가
print(l1)
l1[0:0] = [0] # 인덱스 0번쨰에 0을 추가
print(l1)
for i in l1:
    print(i)