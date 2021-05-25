gender = input(("남/여 중에 하나를 입력하세요"))
cnt = int(input("팔굽혀 펴기 횟수를 입력하세요"))
if gender == "남":
    if cnt > 10:
        grade= "합격"
    else:
        grade="꺼져"
else:
    if cnt >= 5:
        grade = "합격"
    else:
        grade = "불합격"

print(f"성별은 {gender}자이고 팝굽히기 횟수는 {cnt}이고 결과는 {grade}입니다")
