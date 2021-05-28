import copy
a = [1, 2, 3]
b = a # 주소를 전달
c = list(a) # 값을 전달
d = copy.copy(a) # 값을 목사해서 전달
a[0] = 11
print(a)
print(b)
print(c)
print(d)