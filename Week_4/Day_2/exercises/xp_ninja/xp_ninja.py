import sys
import random
from copy import copy

user_string = input("Please write something 10 characters long: ")
if not len(user_string) == 10:
    print("You must enter something that is 10 characters long.")
    sys.exit(1)

info = f"First character: {user_string[0]}, Last character: {user_string[-1]}"
print(info)

for i in range(1, len(user_string)+1):
    print(user_string[:i])


jumbled = list(copy(user_string))
random.shuffle(jumbled)
jumbled = ''.join(jumbled)
print("Jumbled string: {}".format(jumbled))