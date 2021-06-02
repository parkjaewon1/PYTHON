def YourRange(start, end):
     current = start
     while current < end: # return은 함수를 종료하고 감ㅅ을 전달
         yield current  # 함수를 종료하지 않고 중간 멈춰서 값을 전달하고 다시 실행
         current += 1
     return
for i in YourRange(0, 5):
    print(i)