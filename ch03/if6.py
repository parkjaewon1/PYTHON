print("점수를 입력하세요")
score = int(input())

if score >= 60:    message = "합격"
else:    message = "불합격"
print(f"점수는 {score}이고 결과는 {message}입니다")

msg = "합격" if score >= 60 else "불합격"
print(f"점수는 {score}이고 결과는 {msg}입니다")