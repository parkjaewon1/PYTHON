d1 =  {} # {} dictionary
print(type(d1))
# key는 중복 금지
d1[5] = 25  # dict명[키]=값
d1[2] = 4
d1[3] = 9
d1[3] = 12 # key가 같으면 앞의 key해당하는 값을 덮어쓴다
print(d1)
print(d1[5])
print(d1.get(3)) # get(키)
print(d1.get(4)) # key에 해당하는 값이 없으면 None
print(d1.get(4, '대박')) # 해당하는 값이 없을 때 default로 보여주는 값
print(5 in d1)     # in key에 있는지 여부
print(4 in d1)
print(5 not in d1) # not in은 key 없는지 여부
print(4 not in d1)
print(d1.keys())
print(d1.values())
d1.clear()
print(d1)