num = [1,2,3,4,5]
result =[]
#[2, 4, 6, 8, 10]
result2 =[]
for i in num:
    result.append(i*2)
print(result)

for i in num:
    if i%2 ==1:
        result2.append(i*2)
print(result2)
