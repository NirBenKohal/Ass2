# This is a sample Python script.

# שאלה 1:
def two_sum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((i, j))
    return result

#print(two_sum([1, 2, 3, 4], 7))

# שאלה 2:
def unique(x, y):
     unique = [[1, 5], [1, 10], [10, 50], [10, 100], [100, 500], [100, 1000]]
     if [x, y] in unique:
         return True
     else:
         return False

def roman_to_int(s):
    s = s.replace(" ", "").upper()
    lst = list(s)
    total = 0

    for i in range(len(lst)):
        if lst[i] == 'I':
            lst[i] = 1
        elif lst[i] == 'V':
            lst[i] = 5
        elif lst[i] == 'X':
            lst[i] = 10
        elif lst[i] == 'L':
            lst[i] = 50
        elif lst[i] == 'C':
            lst[i] = 100
        elif lst[i] == 'D':
            lst[i] = 500
        elif lst[i] == 'M':
            lst[i] = 1000

    for i in range(len(lst)-1):
        if unique(lst[i], lst[i+1]):
            total = total - lst[i]
        else:
            total += lst[i]
    total += lst[len(lst)-1]
    return total


s = ('IIIIIIIII')
print(roman_to_int(s))

# שאלה 3:
def plus_one(digits):
    str_neg = 'The given input is not a numerical list!'
    if type(digits) is not list:
        return str_neg
    for i in range(len(digits)):
        if type(digits[i]) != int or not (0 <= digits[i] <= 9):
           return str_neg

    result = len(digits) * [9]
    if digits == result:
        result = len(digits) * [0]
        result.insert(0, 1)
        return result

    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    return digits

#digits = [9, 9, 9, 9, 9]
#print(plus_one(digits))



#שאלה 4:
def convert(s, len_of_row):
   string_list = []
   for i in range(len_of_row):
       text = s[i::len_of_row]
       string_list.append(text)

   return "".join(string_list)

#print(convert("super duper", 4))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
