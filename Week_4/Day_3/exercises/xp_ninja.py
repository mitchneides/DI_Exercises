# 1,yair

# import string
# import random
#
# letters = string.ascii_letters
# integers = [random.randint(1, 100000) for i in range(10)]
# strings = [''.join(random.choices(letters, k=5)) for i in range(10)]
#
# l = integers + strings
# random.shuffle(l)
#
# string_list = []
# int_list = []
# for element in l:
#     if type(element) == str:
#         string_list.append(element)
#     else:
#         int_list.append(element)
#
# print(l)
# print(string_list)
# print(int_list)

#1,me
# list = [1,'hello',2,'there',3,'how are you?']
# ints = []
# strings = []
# for item in list:
#     if type(item) == str:
#         strings.append(item)
#     else:
#         ints.append(item)
#
# print(ints)
# print(strings)

# 2,me
# somestring = 'Hello how are you doing? '
# somelist = []
# while ' ' in somestring:
#     pos = somestring.index(' ')
#     somelist.append(somestring[0:pos])
#     somestring = somestring[(pos+1):(len(somestring))]
#
# print(somelist)

# 3,yair
# import string
# import random
#
# letters = string.ascii_letters
# strings = [''.join(random.choices(letters, k=random.randint(1, 10))) for i in range(10)]
# print(strings)
#
# max_length = 1
# for index, s in enumerate(strings):
#     temp = len(s)
#     if temp > max_length:
#         max_length = temp
#         long_index = index
#
# print(strings[long_index])
#
# print(max_length)
# # or:
# print(sorted(strings, key=len)[-1])

#3,me
# words = ['hello','there','have','a','wonderful','day']
# longest = ''
# for word in words:
#     if len(word)>len(longest):
#         longest = word
#
# print("Longest word is: " + longest)

# 4,me
# password = input("Enter a password: ")
# plen = len(password)
# star = '*'
# hidden = plen*star
# print("Password: "+hidden)

# 5,me
# sandy_orders = ['tuna','turkey','cheese','pb&j']
# finished_sandys = []
#
# for sandy in sandy_orders:
#     print(f"I made your {sandy} sandwich")
#     finished_sandys.append(sandy)
#
# string = ''
# for word in finished_sandys:
#     if word != finished_sandys[-1]:
#         string = string+word+", "
#     else:
#         string = string+"& "+word+"."
#
# print("The following sandos were made: "+string)

# 6,me
# sandy_orders = ['pastrami','tuna','turkey','pastrami','cheese','pb&j','pastrami']
# print("Deli has run out of pastrami :(")
# while 'pastrami' in sandy_orders:
#     sandy_orders.remove('pastrami')
#
# finished_sandys = []
#
# for sandy in sandy_orders:
#     print(f"I made your {sandy} sandwich")
#     finished_sandys.append(sandy)
#
# string = ''
# for word in finished_sandys:
#     if word != finished_sandys[-1]:
#         string = string+word+", "
#     else:
#         string = string+"& "+word+"."
#
# print("The following sandos were made: "+string)

# 7,me
# user_str = input("Enter a string to be ciphered: ")
# cipher_num = input("Enter a number for the cipher: ")
# ciphered_str = ''
# count = 0
# while count<len(user_str):
#     letter = user_str[count]
#     num_of_letter = ord(letter)
#     new_letter = chr(num_of_letter+int(cipher_num))
#     ciphered_str = ciphered_str+new_letter
#     count += 1
#
# print("Ciphered string: "+ciphered_str)
#
# rev_str = input("Enter a string to be de-ciphered: ")
# decipher_num = input("Enter the number for the de-cipher: ")
# deciphered_str = ''
# rev_count = 0
# while rev_count<len(rev_str):
#     rev_letter = rev_str[rev_count]
#     num_of_rev_letter = ord(rev_letter)
#     unrev_letter = chr(num_of_rev_letter-int(decipher_num))
#     deciphered_str = deciphered_str+unrev_letter
#     rev_count += 1
#
# print("Deciphered string: "+deciphered_str)

# 8,me
# i = 1
# star = '*'
# while i<6:
#     print(star*i)
#     i+=1
# space = " "
# j=0
# t=5
# while j<6:
#     print(space*j+star*t)
#     j+=1
#     t-=1

# 9,me
# space = " "
# sp = 2
# star = "*"
# st = 1
#
# while st<=5:
#     print(space*sp + star*st + space*sp)
#     sp-=1
#     st+=2

#10
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)



