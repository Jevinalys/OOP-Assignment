# Person class

class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def Introduce(self):
        print(f'Hello my name is {self.name} I am a {self.age} years old {self.gender}')

newPerson = Person("Jevinalys",29,"Male")
newPerson.Introduce()
