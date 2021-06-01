class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("야홍")
    def drink(self, food):
        print(f"{self.name}이 {food}를 먹는다")

cat1 = Cat("냥이"); cat2 = Cat("옹이")
cat1.speak();  cat1.drink("우유")
Cat.speak(cat2); Cat.drink(cat2, "막걸리")