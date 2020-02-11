# class Writer:
#
#     def __init__(self, name, n_books, genre):
#         self.name = name
#         self.n_books = n_books
#         self.genre = genre
#
#     def write(self):
#         self.n_books += 1
#         print(f"{self.name} wrote a book.")
#
#     @staticmethod
#     def say_hi():
#         print("Hi!")  # Don't need information of the instance (ie: self) to run this
#
#
# class Philosopher(Writer):
#
#     def __init__(self,name, n_books, genre, domain):
#         super().__init__(name, n_books, genre) #makes the init of the parent class work down here along with:
#         self.domain = domain #the new parameter we want to introduce
#
#     def write_nonsense(self):
#         self.n_books += 1
#         print(f"{self.name}: What is this nonsense.")
#
#
# class French:
#
#     def __init__(self,name):
#         self.name = name
#
#     def talk_nonsense(self):
#         print(f"{self.name}: bla bla...nonsense...bla")
#
#
# class FrenchPhilosopher(Philosopher, French): #init comes from writer because philos gets from writer and is declared first
#
#     def conference(self):
#         print(f"{self.name}: ...Post modern conference nonsense")
#
#
# if __name__ == '__main__':
#
#     albert = Writer(name="Albert Camus", n_books=25, genre=["Philosophy", "Roman"])
#     print(albert.name)
#     print(albert.n_books)
#     print(albert.genre)
#
#     albert.write()
#     print(albert.n_books)
#     albert.say_hi()
#
#     fred = Philosopher(name="Fred", n_books=30, genre=["Amoralism", "Uberstuff"],domain="Something")
#     print(fred.n_books)
#     fred.write()
#     print(fred.n_books)
#     fred.write_nonsense()
#     print(fred.n_books)
#
#     derrida = FrenchPhilosopher(name="Jacques Derrida",n_books=200,genre=['Post modernism'],domain="Philology")
#     derrida.conference() #from french philos
#     derrida.talk_nonsense() #from french
#     derrida.write() #from writer
#     derrida.write_nonsense() #from philos
#     print(derrida.domain)



# import math
#
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius**2
#
#
#     @staticmethod
#     def compute_area(r):
#         return math.pi * r**2
#
#
# if __name__ == '__main__':
#     c = Circle(radius=2)
#     print(c.area())
#     print(c.compute_area(r=5))


# def decorator(func):
#     def wrapper():
#         print(f"running {func}")
#         func()
#         print("Done")
#
#     return wrapper
#
# @decorator
# def talk():
#     print("Talking")
#
# if __name__ == '__main__':
#
#     talk()


import time

def decorator(func):
    def wrapper():
        print(f"running {func}")
        func()
        print("Done")

    return wrapper

@decorator
def talk():
    print("Talking")



def timeit(func): #defines decorator, saying that every time it is called it will take time, call the func that is put in, then take the time again
    def wrapper(*args, **kwargs): #args and kwargs covers any possible thing that can be required for the function to run
        start = time.perf_counter()
        output = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"function took: {end}")
        return output
    return wrapper

@timeit #says that the following function should be executed within the wrapper
def compute(power):
    return 2**power


if __name__ == '__main__':

    # talk()
    out = compute(9)
    print(out)