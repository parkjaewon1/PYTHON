# with와 같이 오픈하면 작업이 종료되면 자동으로 close된다
with open('voca.txt','r', encoding='utf-8') as file:
    for i in file:
        data = i.strip().split(": ")
        kor = data[1]
        eng = data[0]
        print(f"{kor}에 해당하는 영어는 ?")
        eng_ans = input()
        if eng == eng_ans:  print("잘했어 칭구")
        else:     print(f"으이그 그것도 몰라 답은 {eng}야")
    print("프로그램 종료")