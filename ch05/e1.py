a, *b = [1, 2, 3, 4,5] # 1은 a, 나머지 모두 b
print(a)
print(b)
*a, b = [1, 2, 3, 4,5] # 5은 b, 나머지 모두 a
print(a)
print(b)
a, *b, c = [1, 2, 3, 4, 5] # 1은 a, 5는 c, 나머지는 b
print(a)
print(b)
print(c)
# a, *b, *c = [1, 2, 3, 4, 5] # b와 c에 들어갈 갯수가 불명확 하므로 에러