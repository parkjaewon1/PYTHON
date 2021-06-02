class Person:
    def speak(self):      print("떠든다")
    def move(self):       print("두발로 움직인다")
class Fish:
    def move(self):       print("지느러미로 헤엄친다")
class MurMaid(Person, Fish): # 메서드가 중복된 경우 먼저 상속받는 메서드가 우선권이 있다
    pass

mm= MurMaid()
mm.speak()
mm.move()