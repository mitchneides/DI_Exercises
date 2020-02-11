import math
import random

#
#
# class Circle:
#     def __init__(self, radius=1.0):
#         self.radius = radius
#
#     @classmethod
#     def get_perimeter(cls,radius):
#         perimeter = 2 * math.pi * radius
#         print(perimeter)
#         return perimeter
#
#     @classmethod
#     def get_area(cls, radius):
#         area = math.pi * radius**2
#         print(area)
#         return area
#
#
# class MyList:
#     def __init__(self,l):
#         if len(l)>0:
#             self.list = l
#
#     def reversed_list(self):
#         print(self.list[::-1])
#         return self.list[::-1]
#
#
#     def sorted_list(self):
#         print(sorted(self.list))
#         return sorted(self.list)
#
#     def gen_rand_list(self):
#         rand_list = []
#         for item in self.list:
#             rand_list.append(random.randint(1,9))
#
#         print(rand_list)
#         return rand_list
#
#
# if __name__ == '__main__':
#
#     # circle1 = Circle(3)
#     # circle1.get_area(3)
#     # Circle.get_perimeter(3)
#     # Circle.get_area(3)
#     l1 = MyList([1,9,4,2,6,8])
#     l1.reversed_list()
#     l1.sorted_list()
#     l1.gen_rand_list()


class QuantumParticle:
    def __init__(self, position, momentum, spin):
        self.position = position
        self.momentum = momentum
        self.spin = spin

    def measure_position(self):
        pos = random.randint(1,100)

        return pos

    def measure_momentum(self):
        moment = random.uniform(1,100)
        return moment

    def measure_spin(self):
        choice = random.randint(0,1)
        if choice == 0:
            s = 0.5
        else:
            s = -0.5
        return s




if __name__ == '__main__':
    q = QuantumParticle(2,2,0.5)
    print(q.measure_momentum())
    print(q.measure_position())
    print(q.measure_spin())