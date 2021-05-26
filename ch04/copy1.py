x=[2,3,5,7,11]
k=list(x) # list 함수를 사용하면 값을 복사한다 
y=x   # 이 경우 값이 아닌 주소를 복사하기 때문에 값이 같아진다
y[2] = 77
print(x)
print(y)
print(k)