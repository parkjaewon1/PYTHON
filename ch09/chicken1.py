file = open('chicken.txt','r', encoding='utf-8')
# print(type(file))
for i in file:
    print(i, end="")
file.close()