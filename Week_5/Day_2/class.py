class Animal:
    def __init__(self, l, c, h, n):
        self.legs = l
        self.color = c
        self.height = h
        self.name = n
        self.sleeping = False

    def sleep(self):
        self.sleeping = True
        return f"{self.name} is sleeping."

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):
# this means that dog will take on all the properties that animal is a blueprint for
    def bark(self):
        return f'{self.name} barks!'


class Shark(Animal):
    def sleep(self):
        return 'Sharks do not sleep.'



# a = Animal(4, "Brown", "3 Meters", "Titan")
# print(a.sleeping)
# print(a.sleep())
# print(a.sleeping)

# dog = Dog(4,"Red","50cm", "Sparky")
# print(dog.sleep())
# print(dog.bark())

shark = Shark(0,"White",'50cm','Elvis')
print(shark.sleep())




# # kwargs
# def born(self, **kwargs):
#     member = {}
#     for key, value in kwargs.items():
#         member.update({key:value})
#     self.members.append(member)
#
# f = Family('fam')
# f.born(name='Jim', sex= 'male')
# # no matter how many key/value pairs listed in this call, kwargs will take them all and
# # add them to the dictionary