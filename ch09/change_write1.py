with open('test2.txt','w',encoding='utf-8') as f1:
    # print할 때 file 뒤에 file과 연결하면 콘솔이 아니라 파일에 저장
    print("대박 1 ", file=f1)
    print("사건 1 ", file=f1)
with open('test2.txt','w',encoding='utf-8') as f1:
    print(f1.read())