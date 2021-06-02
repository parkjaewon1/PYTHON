class A:
    def m1(self):
        print("대박")
class B(A):
    def m1(self):
        print("허걱")
class C(A):
    def m1(self):
        print("허각")
a = A(); b = B(); c = C()
a.m1(); b.m1(); c.m1()