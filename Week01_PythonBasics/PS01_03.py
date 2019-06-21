s = 'aabbccddeeffggzcbobobegghaklABCDEFGH'
#s = 'abcbcd'
# s = 'deeebskdj'
# s = 'zyxwvutsrqponmlkjihgfedcba'
# s = 'aafgmzmfmw'
s = 'eamqyrtmgwe'


s = s.lower()
s = s[::-1]
print(s)
length_piece_string = 1
max_length_string = 0
position = 0
for char_position in range(len(s)-1):
    if s[char_position] >= s[char_position+1]:
        length_piece_string += 1
        if length_piece_string >= max_length_string:
            max_length_string = length_piece_string
            position = char_position+1
    else:
        length_piece_string = 1

print(max_length_string)
print(position)

if length_piece_string == 1:
    longest_substring = s[0]
else:
    longest_substring = s[position-max_length_string+1:position+1]


print('Longest substring in alphabetical order is: {}'.format(
    longest_substring[::-1]))
