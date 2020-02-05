# matrix = '''
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
# '''
#
# l = list(matrix)
#
#
# # print(l)
# # how_many_cols = 1
# # while list[0] != list[how_many_cols]:
# #     how_many_cols += 1
# #
# # print(how_many_cols)
# #
# # num_of_rows = l.count('\n')
# # print(num_of_rows)
# # print(len(l))
#
#
#
# for thing in l:
#     if thing == '\n':
#         l.remove(thing)
#
# col1 = []
# col2 = []
# col3 = []
#
# def add_to_temp_lists(start_num,column):
#     for thing in range(start_num,len(l)-1,3):
#         if l[thing].isalpha():
#             column.append(l[thing])
#         if l[thing] == '$' or l[thing] == '#' or l[thing] == '%':
#             column.append(' ')
#
#
# add_to_temp_lists(0,col1)
# add_to_temp_lists(1,col2)
# add_to_temp_lists(2,col3)
#
# all_together = col1+col2+col3
# print(all_together)
# i = 0
# while i<len(all_together):
#     j = i + 1
#     if all_together[i] == ' ' and all_together[j] == ' ':
#         del all_together[j]
#     i += 1
#
#
# print(all_together)
#
#
# string_together = ""
# string_together = string_together.join(all_together)
#
# print(string_together)



import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

half_target = target_number // 2
correct_nums = []
for num in range(half_target,target_number):
    if num in list_of_numbers:
        correct_nums.append(num)

pairs = [(target_number-num, num) for num in correct_nums]

print(pairs)
print(len(pairs))

