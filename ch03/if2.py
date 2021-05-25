import sys
print("정수를 입력하세요")
num = int(input())
# 파이썬은 0 또는 데이터가 없으면 False
if num:
    print('반가워')
else:
    print("누구세요")
    sys.exit(0)
print('작업끝')