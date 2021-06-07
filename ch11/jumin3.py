import re
while True:
    print('주민 번호를 입력하세요')
    no = input()
    if no == 'q':     break
    p = re.search('\d{6}-\d{7}')
    if p.search(no) != None: # 일치하면
        print("주민번호입니다")
    else:      print("주민번호가 아닙니다")