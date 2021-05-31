def f(x):
    return x*x
l1 = [1, 2, 3, 4, 5]
print("반복문을 사용하여 함수 실행")
for i in l1:
    print(f(i), end=" ")
print("\n map을 이용한 함수 실행")
# map(함수, 값) list에 있는 각각의 값을 하니씩 함수에 대입하여 실행하고 결괴를 list로 한다
result = list(map(f, l1))
print(result)
print("lamda와 map을 같이 사용")
result = list(map(lambda x:x*x, l1))
print(result)
