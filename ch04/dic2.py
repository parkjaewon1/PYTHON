keys = ['one', 'two', 'three']
values = (1, 2, 3)
d1 = dict(zip(keys, values))
print(d1)
for i in d1:
    print(i,":",d1[i])