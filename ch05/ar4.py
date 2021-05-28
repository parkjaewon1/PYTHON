def ar(*args, len): # 값만 전달
    for i in range(len):
        print(args[i])
ar("대박", "사건", "야호", "금요일", len=4)