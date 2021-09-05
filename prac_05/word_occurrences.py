"""
Practical 5 - Samuel Barrett
Word Occurrences program
"""

cnt = 1
user_str = input("Text: ")

user_str_list = user_str.split()
user_str_dict = {}
# print to see how this works
# print(user_str_list)


for word in user_str_list:
    total = user_str_dict.get(word, 0)
    user_str_dict[word] = total + 1
    # print to see how this works
# print(user_str_dict)


user_str_list = list(user_str_dict.keys())
user_str_list.sort()
# print to see how this works
# print(user_str_list)


spacing = max((len(word) for word in user_str_list))
for word in user_str_list:
    print("{:{}} : {}". format(word, spacing, user_str_dict.get(word)))

