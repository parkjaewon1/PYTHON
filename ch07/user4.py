class User:
    # __init__ 자바의 생성자와 유사
    def __init__(self, name, age, email):
        self.name = name; self.age=age; self.email = email
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User("영희", 28,"k1@k.com"); user2 = User("철수", 51,"k2@k.com");
user3 = User("길동", 23,"k3@k.com")
user1.introduce(); User.introduce(user2); user3.introduce()