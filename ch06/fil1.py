l1 = [1, 2, 3, 4, 5]
print('lambda와 filter사용')
result = list(filter(lambda x:x%2==0, l1))
print(result)