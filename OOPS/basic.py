#class name should be always starts with capital i each word 
class Student:
    # def __init__(self) ->None:

    idd=0
    name=""
    age=0
    gender=""

    def setDeatils(self):
        self.id=20
        self.name="siddu"
        self.age=65
        self.gender="male"
        self.address="mysore"

    def display(self):
        print(self)
        print(f"self of id = {self.idd}")
        print(f"self of name = {self.name}")
        print(f"self of gender = {self.gender}")
        print(f"self of age = {self.age}")
        print(f"slef of address={self.address}")
s1=Student()
s1.setDeatils()
s1.display()
s2=Student()
s2.display()



