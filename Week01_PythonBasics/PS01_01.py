s = 'azcbobobegghaklA'
vowels = 'aeiou'
count = 0
for ch in s.lower():
    if ch in vowels:
        count +=1
print('Number of vowels: {}'.format(count))