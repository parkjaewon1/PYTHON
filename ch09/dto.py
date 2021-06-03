import pickle


class Dto:
    def setNum(self, num):
        self.num = num

    def setName(self, name):
        self.name = name

    def getNum(self):
        return self.num

    def getName(self):
        return self.name

    def toString(self):
        return "{번호 :", self.num + ", 이름 :", self.name + "}"

    dat1 = Dto();
    dat1.setNum(1);
    dat1.setName("kim")
    dat2 = Dto();
    dat2.setNum(2);
    dat2.setName("park")
