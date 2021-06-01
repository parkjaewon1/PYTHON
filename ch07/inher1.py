class P1:
    def __init__(self, name):
        print("P1.__init__()")
        self.message = "안녕"
        print(name)
    def pr(self):
        print("대박")
# 자바에서는 자식을 생성하면 부모의 생성자가 먼저 실행하고 그 다음에 자식 생성자가 실행
# 파이썬은 부모의 생성자를 실행시키지 않는다
class C1(P1):
    def __init__(self):
        super().__init__("영미")
        print("C1.__init__()")
        # 부모의 생성자를 호출하여 실행시킨다.
        # 자바에서는 부모 호출하는 메서드가 첫째줄 이지만 파이썬은 관계없다

        print("메세지 : "+self.message)
ob = C1()
ob.pr()