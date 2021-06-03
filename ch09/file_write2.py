# 'w'로 파일을 open 하면 기존 데이터 삭제
file = open('test.txt', 'w', encoding='utf-8')
file.write("대박사건\n")
file.write("오후에 비온대\n")
file.close()
# 'a'로 파일을 open 하면 기존 데이터 그대로 있고 뒤에 데이터 추가
file = open('test.txt', 'a', encoding='utf-8')
file.write("대박사건\n")
file.write("오후에 비온대")
file.close()