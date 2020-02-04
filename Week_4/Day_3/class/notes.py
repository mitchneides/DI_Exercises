#if statements

# l = [1, 2, 3, 45, 96]
#
# if 1 in l:
#     print("Yes")
# elif 0 in l:
#     print("No")
# else:
#     print("Don't know")


# l = [1, 2, 6, 0]
#
# if all(l):
#     print("yes")
# elif any(l):
#     print('not all')
# else:
#     print("no")
#all is false because 0==false
#any is true because at lease 1 number is true (not 0)


# l = ['u', 4, [3,2,1], {'a':78}]
#
# for index in range(len(l)):
#     print(index, l[index])


# for i in range(11):
#     if i%2 == 0:
#         print(i)
#     elif i == 5:
#         print(i)
#         break
#     else:
#         continue

# i=0
# while i<10:
#     print(i)
#     i+= 1

# while True:
#     value = int(input("Input a number between 1 and 10: "))
#     if 1<=value<=10:
#         print("Thanks")
#         break
#     else:
#         print("Not in the valid range. Please try again...")

#
# while True:
#     value = input("Input a number between 1 and 10: ")
#     try:
#         value = int(value)
#     except ValueError:
#         print("Not a number. Try again...")
#         continue
#
#     # can also use:
#     # if not value.isdigit():
#     #     print("Not a number. Try again...")
#     #     continue
#
#     if 1<=value<=10:
#         print("Thanks")
#         break
#     else:
#         print("Not in the valid range. Please try again...")
#

#     #useful tricks:
# print([num for num in range(10)])
# print([num*2 for num in range(10)])
# print(sum([num*2 for num in range(10)]))
# print([num*2 for num in range(10) if num%2 == 0])
# print(list(zip(range(5),range(5))))
# print({str(key):value for key,value in zip(range(5),range(5))})
#
# names = ["John","Eyal","Michael"]
# ages = ["20","30","35"]
# print({name:age for name,age in zip(names,ages)})
#
# print(ages)
# print(list(map(int,ages)))






