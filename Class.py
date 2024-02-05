class Animal:
    def walk(self):
        print("walking.....")


class Cat(Animal):
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def bark(self):
        print('woof')


roger = Cat('Roger',23)

print(type(roger))
print(roger.name)
print(roger.age)
print(roger.bark())
print(roger.walk())

