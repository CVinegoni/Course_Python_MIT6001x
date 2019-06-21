# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
string_to_search = 'bob'
occurring_number = 0
for position in range(len(s)-len(string_to_search)+1):
    print(s[position:position+len(string_to_search)])
    if s[position:position+len(string_to_search)] == string_to_search:
        occurring_number += 1
print('Number of times bob occurs is: {}'.format(occurring_number))


