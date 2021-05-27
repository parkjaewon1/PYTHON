x = {'a':30, 'b':20, 'c':50}
for i in x:  # x에서 key만 가져 온다
    print(i, ":", x[i] )
print("===============")
for i in x.keys():  # x에서 key만 가져 온다
    print(i, ":", x[i] )
print("===============")
for i in x.values():  # x에서 value만 가져 온다
    print(i )
print("===============")
for i , j in x.items():  # x에서 key와 값을 가져와서 i애는 key, j에는 값
    print(i, ":",j )