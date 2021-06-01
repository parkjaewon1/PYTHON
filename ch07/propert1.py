class Student: # __는 의미가 나는 private이라는 뜻
    def __init__(self, name="무명"):       self.__name = name
    def setName(self,name):
        print("setter methodd호출")
        self.__name = name
    def getName(self):
        print("getter method호출")
        return self.__name
    def setAge(self,age):
        print("setter methodd호출")
        if age < 0:
            print("나이가 음수가 어디있어")
            self.__age = 0
        else:          self.__age = age
    def getAge(self):
        print("getter method호출")
        return self.__age
    name = property(fset=setName, fget=getName)
    age = property(getAge, setAge) # get을 먼저 사용하면 fset, fget생략 가능
st1 = Student("모모")
print(st1.name)
st1.name = "철수"
st1.age = -10
print(f"이름 : {st1.name}, 나이 : {st1.age}")