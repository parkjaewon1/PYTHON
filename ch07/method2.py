class Couter:
    count = 0 # 클래스 변수는 누적이 가능
    def __init__(self):
        Couter.count += 1
    @classmethod
    def print_count(cls):
        print(cls.count) # cls사용하면 클래스 변수를 읽을 수 있다
c1 = Couter(); c2 =Couter(); c3 = Couter();
c3.print_count()
Couter.print_count()