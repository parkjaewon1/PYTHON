#    012345
a = 'Pithon'
# i가 y로 변경
# 문자열은 이부만 변경이 안됨
# a[1] = 'y'
print(a[:1]+'y'+a[2:])
#      0123456789012
str = "Hardware and Shell"
print(str[:8]+' Kernel'+str[12:])
print(str[:8]+str[12:])