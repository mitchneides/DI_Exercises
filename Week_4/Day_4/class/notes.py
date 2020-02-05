# import random

# def talk():
#     p = random.random()
#     if p > 0.5:
#         return "Whatever"
#     else:
#         print("Coin toss")
#         return "Something else"
#
#
# output = talk()
# print(output)


# def multiply_2(num=2, multiplier=5):
#     return num * multiplier
#
#
# mul = [multiply_2(2, multiplier) for multiplier in range(1,11)]
# print(mul)

# output = multiply_2(9,9)
# print(output)

# mul = []
# def twos():
#     for num in range(2,21,2):
#         mul.append(num)
#
#
# twos()
# print(mul)


# person = "Yair"
#
#
# def say_name(person):
#     person += " something"
#     other_guy = "Shlomo"
#     print(f"Hey {person}")
#     return other_guy
#
#
# say_name(person)
# print(person)
# print(other_guy)


# def show_names(*args):
#     for i, name in enumerate(args):
#         if type(name) == str:
#             print(f"Person number {i}: {name}")
#         else:
#             print("Error")
#
#
# show_names('Yair', 'Shlomo', 'Eran', 'Rachel', 'Lior', 'Mitchell', 2)

# def show_info(**kwargs):
#     for key,value in kwargs.items():
#         print(key+":", value)
#
#
# info = {'name': 'Fred', 'last name': 'Nietzsche', 'profession': 'philosopher', 'nationality': 'german'}
#
# show_info(name='Jon', last_name='Deer', profession='farmer')


# def operation(num1,num2,**kwargs):
#     if kwargs:
#         print(f"Description:\n {kwargs}")
#     return num1 ** num2
#
#
# result = operation(2, 3, description='2 to the power of 3', type='mathematical')



# YEAR = 2020
# MONTH = 2
#
#
# def get_age(year: int, month: int, day: int):
#     if month > MONTH:
#         age = YEAR - year - 1
#     else:
#         age = YEAR - year
#     return age
#
#
# # print(get_age(1990, 3, 1))
#
#
# def can_retire(sex, date_of_birth):
#     args = list(map(int, date_of_birth.split('/')))
#     month, day, year = args[0], args[1], args[2]
#     age = get_age(year, month, day)
#     print(f"Your age: {age}")
#     if sex.lower() == 'm':
#         return age >= 67
#     else:
#         return age >= 62
#
#
# if __name__ == "__main__":
#     print("Can you retire in Israel? Answer the following questions: ")
#     sex = input("Gender (m/f): ")
#     birthday = input("Enter your birthday (mm/dd/yyyy): ")
#
#     output = can_retire(sex, birthday)
#     if output:
#         print("Happy retirement!")
#     else:
#         print("Sorry baws, you still gotta work.")