a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b))   # 차집합
print(b.difference(a))
print(a.symmetric_difference(b)) # 두개의 집합에서 공통부분 제외한 나머지 전부
print(5 in a)
print(7 in a)
print(5 not in a)
print(7 not in a)