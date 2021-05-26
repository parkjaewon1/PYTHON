
data = ['Morning','Afternoon','evening','Night']
data.sort()
print(data)
data.sort(reverse = True)
print(data)
#대소문자 구별없이 정렬
data.sort(key=str.lower,reverse=True)
print(data)