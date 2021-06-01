class User:
    def initialize(self, name, age, email):
        self.name = name; self.age=age; self.email = email
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User(); user2 = User(); user3 = User()
user1.initialize("영희", 28,"k1@k.com")
user2.initialize("철수", 51,"k2@k.com")
user3.initialize("길동", 23,"k3@k.com")
user1.introduce(); User.introduce(user2); user3.introduce()