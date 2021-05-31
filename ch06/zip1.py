a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]
a = list(zip(a1, a2))
print(a)
s = []
# 두개씩 묶여있는 데이터를 for ~ in을 사요하면 각각 받을 수 있다
for i, j in a:
    s.append(i+j)
print(s)
print('sum[a1] =',sum(a1))
print('sum[a2] =',sum(a2))
print('sum[s] =',sum(s))