a1 = [1, 2, 3]
a2 = [4, 5, 6]
a3 = "123"
print(a1 + a2)
print(a1 * 3) # 반복
print(len(a1)) # 인덱스 갯수
print(str(a1[1])+'hi') # 숫자와 문자의 더하기는 에러
a1[1] = 7 # 배열은 변경 가능
print(a1)
# a3[1] = 7 문자열은 변ㄱ경할 수 없음
del a1[2:] # a1의 인덱스 2 이후 데이터를 삭제
print(a1)
a2.append(8) # append는 맨뒤에 추가
print(a2)
a2.append([2,4])
print(a2)