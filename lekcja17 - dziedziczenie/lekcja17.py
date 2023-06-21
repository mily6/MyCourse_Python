class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age


class Dog(Animal):
    def voice(self):
        print("How How")

class Wolf(Dog):
    def voice(self):
        print("Jestem wilkiem")
        super().voice()

class Cat(Animal):
    def voice(self):
        print("Miau Miau")

dog=Dog("Reksio",10)
print(dog.name)
print(dog.age)
dog.voice()
print("")

wolf=Wolf("Reks",12)
print(wolf.name)
print(wolf.age)
wolf.voice()
print("")

cat=Cat("Azor",11)
print(cat.name)
print(cat.age)
cat.voice()