from functools import reduce
print(reduce(lambda x, y:x+y, [47, 11, 42, 13]))
x = [47, 11,42, 102, 13]
f = lambda a, b : a if (a>b) else b
print(reduce(f, x))