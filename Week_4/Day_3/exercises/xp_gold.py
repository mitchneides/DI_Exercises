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

# 5 link does not exist

# 6
# star = '*'
# space = ' '
# i = 1
# j=[4,3,2,1,0]
# for item in j:
#     print(space*item + star*i)
#     i+=1

# 7
# total = 0
# while True:
#     age = input("Enter your age, or 'c' to checkout: ")
#     if age == 'c':
#         print(f"Your total is ${total}")
#         break
#     age = int(age)
#     if age<3:
#         print("Your ticket is free!")
#     elif 3<=age<=12:
#         total = total+10
#         print("Your ticket costs $10.")
#     else:
#         total = total + 15
#         print("Your ticket costs $15.")

# 8
# l = [0,1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(l)-1:
#     if l[i]%2 == 0:
#         print(l[i])
#     i+=1

# 9
# allowed = []
# while True:
#     name = input("Enter your name, or f to finish: ")
#     if name == 'f':
#         break
#     age = int(input("Enter your age: "))
#     if 16<=age<=21:
#         print("You may enter the movie.")
#         allowed.append(name)
#     else:
#         print("You gotta go home bud.")
#
# print(allowed)

# 10
# l = ['dan','steve','ariel','bar']
# newL = []
# for name in l:
#     age = int(input(f"Enter {name}'s age: "))
#     if age>=16:
#         newL.append(name)
# print(newL)

# 11
# x = 1500
# l = []
# while x<2701:
#     if x%7 == 0 and x%5 ==0:
#         l.append(x)
#     x+=1
# print(l)

# 12
# str = 'kajsdf asdfasdkjh asdfasdf alsdkjfhalse we ea fasdf'
# count = 0
# for letter in str:
#     if letter == ' ':
#         count+=1
# print(count)

# 13
# str = 'kajsdf asdfasdkjh asdfasdf alsdkjfhalse we ea fasdf'
# l = list(str.split())
# print(len(l))

# 14
count_up = 0
count_low = 0

str = 'kajLKJSDsdf asdSSfasdSESkjh asdfSFAasdf alsdkjfASDhalse we eAa fasdf'
for letter in str:
    if letter.isupper():
        count_up+=1
    elif letter.islower():
        count_low+=1

print(f"Upper: {count_up}")
print(f"Lower: {count_low}")
