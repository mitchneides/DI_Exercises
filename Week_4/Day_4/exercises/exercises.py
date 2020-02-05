# # 1
#
# import random
#
#
# def get_random_temp(season):
#     if season == 'Winter':
#         temp = float(random.randint(-10,7))
#     elif season == 'Spring' or season == 'Autumn' or season == 'Fall':
#         temp = float(random.randint(8, 25))
#     else:
#         temp = float(random.randint(25, 40))
#     return temp
#
#
# def main():
#     season = input("What season is it? ")
#     rand_temp = (get_random_temp(season.capitalize()))
#     print(f"The temperature right now is {rand_temp} degrees Celsius.")
#     if rand_temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     if 0<=rand_temp<=16:
#         print("Quite chilly! Don’t forget your coat.")
#     if 16<rand_temp<=23:
#         print("Might want a sweater.")
#     if 23 < rand_temp <= 32:
#         print("Nice day, enjoy!")
#     if 32 < rand_temp <= 40:
#         print("Head to the beach!")
#
#
# main()


# 2

import random

def throw_dice():
    throw = random.randint(1,6)
    return throw


def throw_until_doubles():
    dict = {}
    counter = 1
    while True:
        throw1 = throw_dice()
        throw2 = throw_dice()
        dict[counter] = [throw1,throw2]
        counter += 1
        if throw1 == throw2:
            print(dict)
            return counter-1


def main():
    list = []
    for every in range(1,101):
        list.append(throw_until_doubles())

    print(list)
    sum_throws = sum(list)
    avg = sum_throws/len(list)
    print(f"Total throws: {sum_throws}")
    print(f"Average throws: {avg}")

    # print(f"{every}. ",throw_until_doubles())


main()

