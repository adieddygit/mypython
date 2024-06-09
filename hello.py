class Person:
    status = ["Alive"]
    speaks= ["English"]
    def __init__(self, name, sex, race):
        self.name = name
        self.sex = sex
        self.race = race
    def __str__(self):
        return f'{self.name} is a {self.sex} and is from {self.race}'
    exit
    def age(self, yob):
        return f'{self.name} is {2024 - yob} years old'
    
jane = Person('Jane Doe', 'Female', 'LatinX')
john = Person('John Smith', 'Male', 'White')
jane.speaks.append('Spanish')
    
class Pet(Person):
        def __init__(self, name, sex, race):
            super().__init__(name, sex, race)
            self.type = 'Dog'
            self.status = 'Dead'
            #super().speaks.clear()
            super().speaks.append('Barks')
        
my_pet = Pet('Bingo', 'Male', 'German shepherd')
print(jane)
print(jane.speaks)
print(my_pet.age(2020))

