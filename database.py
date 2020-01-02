# class

class PartyAnimal :
    x=0

    def party(self): # class 안에 함수이므로 method로 불림
        self.x=self.x+1
        print('So far', self.x) # 템플릿을 구축

an = PartyAnimal()
an.party() # an이 self의 매개변수
an.party()
an.party()


class PartyAnimal :
    x=0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x=self.x+1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an=PartyAnimal() # 생성
an.party()
an.party()
an=42
print('an contains', an)





class PartyAnimal :
    x=0
    name=""

    def __init__(self, z): # z는 sally or jim
        self.name=z
        print(self.name, 'constructed')

    def party(self):
        self.x=self.x+1
        print(self.name, "party count", self.x)

s=PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()


