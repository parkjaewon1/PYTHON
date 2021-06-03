file = open ('voca.txt','r',encoding='utf-8')
for i in file:
    data = i.strip().split(":")
    kor = data[1]
    eng = data[0]
    print(f"{kor}에 해당하는 영어는 ?")
    eng_ans = input()

    if eng == eng_ans:
        print("잘했어")
    else:
        print(f"틀렸어 답은{eng}야")

print("종료")
file.close()