#1
# favorite_friuts = input("Enter your favorite fruits, separated by a space: ")
# list_fruits = []
# list_fruits.extend(favorite_friuts.split(' '))
# any_fruit = input("Enter the name of any friut: ")
# if any_fruit in list_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")

# 2
# while True:
#     pw = input("Enter a password: ")
#
#     low_count = 0
#     for letter in pw:
#         if letter.islower():
#             low_count += 1
#
#     up_count = 0
#     for letter in pw:
#         if letter.isupper():
#             up_count += 1
#
#     num_count = 0
#     for thing in pw:
#         if thing.isdigit():
#             num_count += 1
#
#     if not 6<=len(pw)<=12:
#         print("Password must be between 6 and 12 characters. Try again...")
#     elif low_count<1:
#         print("Password must contain at least 1 lowercase character. Try again...")
#     elif up_count<1:
#         print("Password must contain at least 1 uppercase character. Try again...")
#     elif num_count<1:
#         print("Password must contain at least 1 number. Try again...")
#     elif ('$' not in pw) and ('#' not in pw) and ('@' not in pw):
#         print("Password must contain $, # or @. Try again...")
#     else:
#         print("The password you entered, "+pw+", is valid.")
#         break

# 3
# for num in range(3,31,3):
#     print(num)

# 4
# l = [0,1,2,3,4,5,6,7,8,9]
# item = input("Enter an item: ")
# spot = int(input("Enter an index to insert your item into: "))
#
# def insert(item,spot):
#     half1 = l.copy()
#     half2 = l.copy()
#     half1 = half1[0:spot]
#     middle = [item]
#     half2 = half2[spot:len(l)]
#     new_list = half1+middle+half2
#     print(f"New list: {new_list}")
#
# insert(item,spot)

# 5





