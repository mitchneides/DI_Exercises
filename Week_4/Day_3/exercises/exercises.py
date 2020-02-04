# 1
# a = int(input("Enter a value for a: "))
# b = int(input("Enter a value for b: "))
#
# if a>b:
#     print("Hello World")

# 2
# a = int(input("Enter a value for a: "))
# b = int(input("Enter a value for b: "))
# c = int(input("Enter a value for c: "))
# all = [a,b,c]
# all.sort()
# print("The greatest number is: " + str(all[-1]))

# 3
# while True:
#     month = input("Enter a month (from 01 to 12): ")
#     if len(month) != 2 or not month.isdigit():
#         print("Month must be a number in 2-digit format. Try again...")
#         continue
#     elif 3<=int(month)<=5:
#         print("The season is spring!")
#         break
#     elif 6<=int(month)<=8:
#         print("The season is summer!")
#         break
#     elif 9<=int(month)<=11:
#         print("The season is autumn!")
#         break
#     else:
#         print("The season is winter!")
#         break

# 4
# while True:
#     alpha = input("Enter a character: ")
#     vowels = ['a','e','i','o','u']
#     if len(alpha)>1:
#         print("You can only enter 1 character. Try again...")
#         continue
#     elif alpha.isdigit():
#         print("You must enter a character. Try again...")
#         continue
#     elif vowels.count(alpha)>0:
#         print(alpha +" is a vowel")
#         break
#     else:
#         print(alpha + " is a consonant")
#         break

# 5
# import random
# num = random.randint(1,9)
# guess = 0
# while int(guess) != num:
#     guess = input("I'm thinking of a number from 1-9. Guess it: ")
#
# print(guess +", you got it!")

# 6
# for num in range(1,21):
#     print(num)

# 7
# some_list = []
# for num in range(1,1000001):
#     some_list.append(num)
#
# for num in some_list:
#     print(num)

# 8
# some_list = []
# for num in range(1,1000001):
#     some_list.append(num)
#
# print(min(some_list))
# print(max(some_list))
# print(sum(some_list))

# 9
# str = '*'
# i = 1
#
# while i<6:
#     print(str*i)
#     i+=1

# 10
# l = [0,2,1,4,1,5,3,1,8,9]
# print(l.index(1))

# 11
# l1 = [1,2,3]
# l2 = ['a','b','c']
# l1.extend(l2)
# print(l1)

# 12
# while True:
#     tops = input("Enter a topping to add to the pizza, or 'o' to put it in the oven: ")
#     if tops == 'o':
#         print("Putting your pizza in the oven now!")
#         break
#     else:
#         print("Adding " +tops +" to your pizza!")

# 13
# while True:
#     age = int(input("Enter your age: "))
#     if age<3:
#         print("Your ticket is free!")
#         break
#     if 3<=age<=12:
#         print("Your ticket costs $10.")
#         break
#     else:
#         print("Your ticket costs $15.")
#         break

# 14
# l = [1,2,3,4,5,6,7,8,9]
# i=len(l)-1
# while i>-1:
#     print(l[i])
#     i-=1

# 15
store = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amanico Ortega Gaona',
    'type_of_clothes': ['men','women','children','home'],
    'international_competitors': ['Gap','H&M','Benetton'],
    'number_stores': 7000,
    'major_color': {'France': 'blue','Spain': 'red','USA': ['pink','green']}
}
store['number_stores'] = 2
print(f"Clients of Zara include {store['type_of_clothes'][0]}, {store['type_of_clothes'][1]} and {store['type_of_clothes'][2]}.")
store['country_creation'] = 'Spain'
if "international_competitors" in store:
    store['international_competitors'].append('Desigual')

store.pop("creation_date")
print(store['international_competitors'][-1])
print(f"The major colors in the US are {store['major_color']['USA'][0]} and {store['major_color']['USA'][1]}.")
print(len(store))
print(store.keys())

store1 = {
    'creation_date': 1975,
    'number_stores': 10000
}

store['number_stores'] = store1['number_stores']
print(store['number_stores'])
store['stores_worldwide'] = {}

def addStore(country, number):
    if 'stores_worldwide' in store:
        store['stores_worldwide'][country] = number

addStore('Jamaica', 3)
addStore('Cuba', 2)
print(store['stores_worldwide'])