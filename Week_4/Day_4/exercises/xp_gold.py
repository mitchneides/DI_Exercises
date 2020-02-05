# 1
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

# 2 - could not find "easy exercise"

# 3
# def describe_city(city, country='Israel'):
#     print(f"{city} is in {country}.")
#
#
# describe_city('Tel Aviv')
# describe_city('Givatayim')
# describe_city('Ohio', "the USA")

# 4 - could not find "easy exercise"

# 8

people = ['Harry', 'Ron', 'Hermione', 'Sirius']


def show_names(*args):
    for i, name in enumerate(args):
        print(f"{i}: ", make_great(name))


def make_great(name):
    return "The Great " + name


show_names(*people)

