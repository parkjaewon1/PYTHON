def ar(len, *args): # 값만 전달
    for i in range(len):
        print(args[i])

# 가변 매개변수 앞에서 호출할 떄는 키워드로 하면 안된다
ar(4, "대박", "사건", "야호", "금요일")