# {대박}을 format과 같이 사용할 경우에는 {{}}로 처리
print("{{대박}}사건이야 이 {}에선".format("동네"))
name = "홍길동"
age = 25
# 파이썬 3.6지원하는 format
print(f"이름은 {name}이고 나이는 {age}")
print(f"이름은 {name}이고 나이는 {age}이지만 내년에는 {age+1}살 입니다")
# java에서 map과 비슷한 것이 파이썬에서는 diction라고 부른다
d = {name:'홍길동', age: 30}
print(f"이름은 {d[name]}이고 나이는 {d[age]}입니다")