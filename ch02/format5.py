name="홍길동"
print(f"안녕 {name:<10}님")
# 10칸을 확보해서 왼쪽부터 출력하는데 빈자리는 @로 채워라
print(f"안녕 {name:@<10}님")
print(f"안녕 {name:@>10}님")
print(f"안녕 {name:@^10}님")
pi = 3.1415923
# pi를 출력하는데 소숫점 2자리까지
print(f"파이 : {pi:0.2f}")