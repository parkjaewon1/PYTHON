# 문장속에 작은 따움표가 있을 경우에는 밖을 큰 따움표로
st1 = "Python's favorite food is perl"
print('st1 = ', st1)
# 밖을 작은 따움표로 했을 경우에는 \를 추가 해야 된다
st2 = 'Python\'s favorite food is perl'
print('st2 = ', st2)
# 문장속에 큰 따움표가 있을 경우에는 밖을 작은 따움표로
st3 = '"Python is very easy." he says.'
print("st3 = ", st3)
# 밖을 큰 따움표로 했을 경우에는 \를 추가 해야 된다
st4 = "\"Python is very easy.\" he says."
print("st4 = ", st4)