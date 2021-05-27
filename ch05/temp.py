def fahrenheit_to_celsius(fahrenheit):
    print("화씨 온도 리스트 :",fahrenheit)
    c = []
    for i in fahrenheit:
        k = (i - 32) * 5 / 9
        c.append(k)
    print("섭씨 온도 리스트 :",c)
# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]
fahrenheit_to_celsius(sample_temperature_list)