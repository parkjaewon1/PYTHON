file = open('test.txt','w', encoding='utf-8')
file.write("Hello\n")
lines = ['안녕하세요', '반갑습니따','파이썬이예요\n']
file.write('\n'.join(lines))
line2 = ['대박\n', '대굴빡\n','빡빡이\n']
file.write(''.join(line2))
file.close()