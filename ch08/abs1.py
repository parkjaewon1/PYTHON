from abc import *
class A1 (metaclass=ABCMeta):  # 추상 클래스
    def prn(self):      print("대박이야")
    @abstractmethod   # 추상 메서드
    def am(self):        pass
# a1 = A1() # 추상메서드는 객체를 생성할 수 없다
class A2(A1):
    def a1(self):      print("대박사건")
    def am(self):      print("난 재정의 했어")
a2 = A2()
a2.a1(); a2.prn(); a2.am()