# class Dog:
#     def __init__(self, nameDog, heightDog):
#         self.nameDog = nameDog
#         self.heightDog = heightDog
#         self.winner = False
#
#     def talk(self):
#         print("Woof!")
#
#     def jump(self):
#         print(f"Jump height: {self.heightDog * 2}cm")
#
#
# Davids_dog = Dog("Rex", 50)
# print(Davids_dog.nameDog)
# print(Davids_dog.heightDog)
#
# Sarahs_dog = Dog("Teacup", 20)
# print(Sarahs_dog.nameDog)
# print(Sarahs_dog.heightDog)
#
# if Davids_dog.heightDog > Sarahs_dog.heightDog:
#     print(f"{Davids_dog.nameDog} is bigger than {Sarahs_dog.nameDog}.")
#     Davids_dog.winner = True
#
# else:
#     print(f"{Sarahs_dog.nameDog} is bigger than {Davids_dog.nameDog}")
#     Sarahs_dog.winner = True
#
# print(Davids_dog.winner)


import string

class Zoo:
    def __init__(self, zooName):
        self.zooName = zooName
        self.animals = []
        self.alpha_pens = {}
        self.num_pens = {}

    def addAnimal(self, newAnimal):
        if newAnimal not in self.animals:
            self.animals.append(newAnimal)

    def getAnimal(self):
        for animal in self.animals:
            print(animal)

    def sellAnimal(self, animal):
        print(f"Goodbye, {animal}")
        self.animals.remove(animal)

    def sortAnimal(self):
        self.alpha_pens = {}
        self.num_pens = {}
        self.animals.sort()
        for animal in self.animals:
            self.alpha_pens[animal[0]] = []
        for animal in self.animals:
            self.alpha_pens[animal[0]].append(animal)

    def getPen(self):
        print()
        print(f"{self.zooName}:")
        print()
        for c, key in enumerate(self.alpha_pens.keys()):
            self.num_pens[c+1] = self.alpha_pens[key]
        for key in self.num_pens.keys():
            print(f"In pen {key}: {self.num_pens[key]}")


myZoo = Zoo("Ohio Zoo")
myZoo.addAnimal("zebra")
myZoo.addAnimal("tiger")
myZoo.addAnimal("hippo")
myZoo.addAnimal("horse")
myZoo.sortAnimal()
myZoo.getPen()
myZoo.sellAnimal('horse')
myZoo.addAnimal('panda')
myZoo.sortAnimal()
myZoo.getPen()
myZoo.addAnimal('horse')
myZoo.addAnimal('gorilla')
myZoo.sortAnimal()
myZoo.getPen()


# another solution:
#
# def sortAnimal(self,animals):
#     sorted_animals = self.animals.sort()
#     print(sorted_animals)
#     temp = 0
#     pen = {}
#     for x,y in zip(animals[::],animals[1::]):
#         if x[0] == y[0]:
#             pen[temp] = [x,y]
#         else:
#             temp += 1
#             pen[temp] = (x)
#             pen[temp] =(y)
#     print(pen)
#
