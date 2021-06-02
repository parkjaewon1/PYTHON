try:
    print("정수를 입력하세요")
    x = int(input())
    y = 100/x
    print(f"나눗셈 결과 :` {y}")
except ZeroDivisionError as err:    print(f"0으로 못나눠 {err}")
except ValueError as err:    print(f"그게 정수냐 {err}")
else: # 에러가 없으면 실행
    print("잘했어")
finally: # 에러 여부와 상관없이 실행
    print("무조건 실행")