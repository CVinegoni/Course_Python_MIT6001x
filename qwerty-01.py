# import string


# def LetterChanges(str):
#     new_string = ''
#     vowels = 'aeiou'
#     for ch in str:
#         if ch in (string.ascii_letters):
#             ch = chr(ord(ch)+1)
#             if ch in vowels:
#                 ch = ch.upper()
#         new_string += ch
#     str = new_string
#     return str


# stringa = 'claud7(&*&(*io'
# print(LetterChanges(stringa))

# import math


# def FirstFactorial1(num):
#     n = num
#     factorial = num
#     while n >= 2:
#         factorial = factorial*(n-1)
#         n = n-1
#     return(factorial)
#     # code goes here


# def FirstFactorial2(num):
#     factorial = 1
#     for indx in range(1, num+1):
#         factorial = factorial*indx
#     return factorial


# def FirstFactorial3(num):

#     # code goes here
#     factorial = 1
#     for indx in range(1, num):
#         num = num*indx
#     return num


# # keep this function call here
# number = 8
# print(FirstFactorial3(number))
# print(math.factorial(number))
# print('caludio')

def Adding(num):
    sum = 0
    for i in range(1, num):
        sum = sum+i
    return sum

print(Adding(10))