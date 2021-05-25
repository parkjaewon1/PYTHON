print("아이디를 입력하세요")
id = input()
print("암호를 입력하세요")
password = input()
if id == "root" and password == "system": # python에서 &&가 아니라 and
    print("로그인 성공")
elif id != "root":
    print("없는 아이디입니다. 누구냐 넌")
else:
    print("암호를 모르네")