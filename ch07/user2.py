class User:
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 이메일 : {self.email}")

user1 = User();  user2 = User(); user3 = User()
user1.name="영희"; user1.age=20; user1.email="k1@k.com"
user2.name="철수"; user2.age=53; user2.email="k2@k.com"
user3.name="길동"; user3.age=25; user3.email="k3@k.com"

User.introduce(user1); User.introduce(user2); User.introduce(user3)
print("====================")
user1.introduce(); user2.introduce();  user2.introduce()