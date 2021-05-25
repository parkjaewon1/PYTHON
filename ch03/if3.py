# print("요일의 첫글자를 입력하세요")
week = input("요일의 첫글자를 입력하세요 : ")
if week=="월":     result="Monday"
elif week=="화":   result = "Tuesday"     # elif는 자바의 else if
elif week=="수":   result = "Wednesday"
elif week=="목":   result = "Thrusday"
elif week=="금":   result = "Friday"
elif week=="토":   result = "Saturday"
elif week=="일":   result = "Sunday"
else : result="바보아냐!  요일도 몰라"
print(result)