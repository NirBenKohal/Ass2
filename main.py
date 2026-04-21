# This is a sample Python script.

# שאלה 1:
# def two_sum(nums, target):
#     tpl1= []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 tpl1.append((i, j))
#     return tpl1

# print(two_sum([1, 2, 3, 4], 7))

# שאלה 2:
# def unique(x, y):
#     unique = [[1, 5], [1, 10], [10, 50], [10, 100], [100, 500], [100, 1000]]
#     if [x, y] in unique:
#         return True
#     else:
#         return False
#
# def roman_to_int(s):
#     #s = s.replace(" ", "").upper()
#     lst = list(s)
#     sum = 0
#
#     for i in range(len(lst)):
#         if lst[i] == 'I':
#             lst[i] = 1
#         elif lst[i] == 'V':
#             lst[i] = 5
#         elif lst[i] == 'X':
#             lst[i] = 10
#         elif lst[i] == 'L':
#             lst[i] = 50
#         elif lst[i] == 'C':
#             lst[i] = 100
#         elif lst[i] == 'D':
#             lst[i] = 500
#         elif lst[i] == 'M':
#             lst[i] = 1000
#     #print(lst)
#
#     for i in range(len(lst)-1):
#         #print(i)
#         if unique(lst[i], lst[i+1]):
#            sum = sum- lst[i]
#            #print(i)
#         else:
#             sum += lst[i]
#         #print(sum)
#     sum += lst[len(lst)-1]
#     return sum
#
#
# s = ('XXVIV')
# print(roman_to_int(s))

# שאלה 3:


# שאלה 4:
def convert(s, len_of_row):

    string_list = []
    for i in range(len_of_row):
        text = s[i::len_of_row]
        string_list.append(text)
        print(string_list)

    return "".join(string_list)

print(convert("super duper", 4))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
