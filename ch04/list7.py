numbers =[]
#1부터 10까지 채우기
numbers[0:0] = range(1,11)
print(numbers)
# 홀수 삭제
del numbers[::2]
print(numbers)
#인덱스 0에 20 추가
numbers.insert(0,20)
print(numbers)

#정렬하여 출력
numbers.sort()
print(numbers)

