"""Wk 4 Practical - Samuel Barrett 13038579"""


# user_name = input('Name: ').capitalize()
# vowels = ['a', 'e', 'i', 'o', 'u']
# cnt = 0
# letter_cnt = len(user_name)
# for i in vowels:
#     if user_name.__contains__(i):
#         cnt += 1
# print('Out of {} letters, {} has {} vowels'.format(letter_cnt, user_name, cnt))

user_name = input('Name: ').capitalize()
vowels = 'aeiouAEIOU'
cnt = 0
letter_cnt = len(user_name) # This is erroneous, can be put straight into print format
for letter in user_name:
    if letter.lower() in vowels:
        cnt += 1
print('Out of {} letters, {} has {} vowels'.format(letter_cnt, user_name, cnt)) # could include len(user_name)
