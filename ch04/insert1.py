a = [1, 2, 3, 2]
a.insert(0,4)
print(a)
a.insert(2, 5)
print(a)
a.remove(2) # 첫번쨰 2의 값 1개을 삭제
print('remove',a)
print(a.pop()) # 마지막 데이터를 끄집어서 출력하고 삭제
print(a)
print(a.pop(0)) # 인덱스 0번째 데이터를 끄집어서 출력하고 삭제
print(a)