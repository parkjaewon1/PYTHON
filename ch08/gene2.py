g1 = [n*n for n in range(21)]
print(g1)
# list와 비슷하지만 소광호로 처리
g2 = (n*n for n in range(21))
# l1 = list(g2)
# print(l1)
print(type(g2))
for i in range(10):
    val = next(g2)
    print(val)
for i in g2:
    print(i)