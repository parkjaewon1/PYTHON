class Person:
    def __init__(self, name, age):    self.name=name; self.age=age
    def prn(self):
        print("===================")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
class Student(Person):
    def __init__(self, name,age, hobby):
        super().__init__(name,age); self.hobby = hobby
    def prn(self):
        super().prn();   print(f"취미 : {self.hobby}")
class Teacher(Person):
    def __init__(self, name,age, major):
        super().__init__(name,age); self.major = major
    def prn(self):
        super().prn();   print(f"과목 : {self.major}")
class Staff(Person):
    def __init__(self, name,age, part):
        super().__init__(name,age); self.part = part
    def prn(self):
        super().prn();   print(f"담당 : {self.part}")
st1 = Student("예린", 25, "울기"); st2=Student("제니", 23, "졸기")
th1 = Teacher("재석", 50, "자바"); th2 = Teacher("호동", 51,"씨름")
sf1 = Staff("아이유",30,"청소");   sf2=Staff("제시", 32,"화장실")
x = [st1, st2, th1, th2,sf1, sf2]
for i in x:
    i.prn()