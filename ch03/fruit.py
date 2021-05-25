print("수박의 무게를 입력하세요")
weight = int(input())  # 입력한 굴자는 무조건 문자로 생가해서 숫자로 형변환
if weight > 10:  result = 1
elif weight > 7: result = 2
elif weight > 4: result = 3
else: result = 4

print(f"입력한 수박의 무게는 {weight}KG이고 {result}등급입니다")