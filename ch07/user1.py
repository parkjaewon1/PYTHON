class User:
    pass

user1 = User();  user2 = User(); user3 = User()
print(type(user1))
print(user1 == user2)
user1.name="영희"; user1.age=20; user1.email="k1@k.com"
user2.name="철수"; user2.age=53; user2.email="k2@k.com"
user3.name="길동"; user3.age=25; user3.email="k3@k.com"
print(user1.name, user1.age, user1.email)
print(user2.name, user2.age, user2.email)
print(user3.name, user3.age, user3.email)
# print(user1.address) # 생성되지 않는 것은 정의 되지 않은 속성