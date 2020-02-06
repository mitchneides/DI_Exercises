# l = [1,34,2346,234,46785,34,99936456,234434]
#
# def find_max(list):
#     max = list[0]
#     for num in list:
#         if num > max:
#             max = num
#
#     print(max)
#     return max
#
#
# find_max(l)


# def factorial(num):
#     total = 1
#     for item in range(num,0,-1):
#         total = total*item
#
#
#     print(total)
#
#
# factorial(10)


# l = [5,4,45,6,31,23]
#
# def list_sum(list):
#     total = 0
#     for num in l:
#         total = total+num
#
#     print(total)
#     return total
#
#
# list_sum(l)


# l = ['a','b','a','b','e','g','a','d','a']
#
# def count_of_something(list, something):
#     count = 0
#     for item in list:
#         if item == something:
#             count += 1
#
#     print(count)
#     return count
#
#
# count_of_something(l,'a')


# l = [3,9,5,2]
#
# def l2_norm(list):
#     total = 0
#     for num in list:
#         total += num**2
#
#     answer = total**0.5
#     print(answer)
#     return answer
#
#
# l2_norm(l)


# l = [0, 1, 2, 4, 8, 9, 90]
# l2 = [90,91,85,33,12,9]
#
#
# def monotonic_check(list):
#     status = True
#     prev_num = list[0]
#     sign = 0
#
#     while sign == 0:
#         for c,num in enumerate(list):
#             sign = list[c] - list[c + 1]
#             if sign != 0:
#                 break
#
#     if sign < 0:
#         for num in list:
#             if num >= prev_num:
#                 prev_num = num
#             else:
#                 status = False
#     else:
#         for num in list:
#             if num <= prev_num:
#                 prev_num = num
#             else:
#                 status = False
#
#     print(f"Answer: {status}")
#     return status
#
#
# monotonic_check(l2)


# string = "racecar"
# string2 = 'not'
# string3 = 'hannah'
# string4 = 'hannnanaah'
#
# def is_palindrome(str):
#     status = True
#     length = len(str)
#     mid_index = length//2
#     l = list(str)
#     start = 0
#     end = length-1
#     while start < mid_index:
#         if l[start] != l[end]:
#             status = False
#             break
#         start += 1
#         end -= 1
#
#     print(status)
#     return status
#
#
# is_palindrome(string4)






