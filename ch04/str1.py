#      01234
str = "Korea"
#    -5-4-3-2-1
print(str[0])      # 인덱스 0
print(str[-2])     # 인덱스 뒤에서 두번째 것
print(str[1:3])    # 인덱스 1부터 3번째 앞까지
print(str[0:5:2])  # 인덱스 처음부터 5번째 2번쨰 건너서
print(str[:-1])    # 마지막 글자를 제외하고 전부
print(str[::-1])   # 처음부터 끝까지 거꾸로
str2 = "Hello "+"World"
print(str2)     # 두문자을 붙인다
print(str2 * 3)  # 3회 반복