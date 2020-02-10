import random

class ForceWielder:
    def __init__(self,name,color=None):
        self.name = name
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)
        self.saber_color = color

    def train(self):
        pass

    def is_jedi(self):
        pass

    def fight(self,opponent):
        harmonic_self = ((self.power**-1 + self.wisdom**-1) / 2)**-1
        harmonic_opponent = ((opponent.power**-1 + opponent.wisdom**-1) / 2)**-1
        if harmonic_opponent>harmonic_self:
            winner = opponent
            loser = self
        else:
            winner = self
            loser = opponent
        print(f"{winner.name} beats {loser.name}")
        return winner


class Jedi(ForceWielder):

    def lightsaber_color(self):
        if self.wisdom > self.power:
            self.saber_color = 'green'
        elif self.wisdom < self.power:
            self.saber_color = 'blue'
        else:
            self.saber_color = 'violet'
        self.wisdom += 10

    def train(self):
        num1 = random.randint(10,20)
        self.wisdom += num1
        num2 = random.randint(5,15)
        self.power += num2

    def is_jedi(self):
        return True


class Sith(ForceWielder):

    def rename(self):
        self.name = "Darth "+self.name
        print(self.name)
        return self.name

    def lightsaber_color(self):
        self.saber_color = 'red'
        self.power += 10

    def train(self):
        num1 = random.randint(10,20)
        self.power += num1
        num2 = random.randint(5,15)
        self.wisdom += num2

    def is_jedi(self):
        return False






Luke = Jedi("Luke")
Luke.lightsaber_color()
Luke.train()
Ben = Jedi("Ben")
Ben.lightsaber_color()
Ben.train()
Yoda = Jedi("Yoda")
Yoda.lightsaber_color()
Yoda.train()

Vader = Sith("Vader")
Vader.rename()
Vader.lightsaber_color()
Vader.train()
Sidius = Sith("Sidius")
Sidius.rename()
Sidius.lightsaber_color()
Sidius.train()
Snoke = Sith("Snoke")
Snoke.rename()
Snoke.lightsaber_color()
Snoke.train()
Snoke.train()
Snoke.train()
Snoke.train()


force = [Luke,Ben,Yoda]
dark = [Vader, Sidius, Snoke]
round = 1
while round<100 and len(dark)>0:
    rand1 = random.randint(0,len(force)-1)
    rand2 = random.randint(0,len(dark)-1)
    winner = force[rand1].fight(dark[rand2])
    if winner in force:
        force[rand1].train()
        dark.pop(rand2)
    else:
        winner.train()
        force[len(force)-1].train()
    round += 1

if round >= 100:
    print("The Sith win")
else:
    print(f"The Jedi win in {round} rounds")