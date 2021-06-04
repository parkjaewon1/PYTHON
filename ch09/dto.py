import pickle
class Dto:
    def setNum(self, num):
        self.num = num
    def setName(self,name):
        self.name = name
    def getNum(self):
        return self.num
    def getName(self):
        return self.name
    def toString(self):
        return "{번호 :"+str(self.num)+", 이름 : "+self.name+"}"
dat1 = Dto(); dat1.setNum(1); dat1.setName("kim")
dat2 = Dto(); dat2.setNum(2); dat2.setName("park")
li = [dat1, dat2]
with open("test3.txt",'wb') as f:
    pickle.dump(li, f)
with open("test3.txt",'rb') as f:
    result = pickle.load(f)
    for i in result:
        print(i.toString())