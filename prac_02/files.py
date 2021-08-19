"""
CP1404
Samuel Barrett - 13038579
"""
# # Quick Program 1
# out_file = open("name.txt", "w")
# name = input("What is your name? ")
# print(name, file=out_file)  # or out_file.write(name)
# out_file.close()

# # Quick Program 2
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# in_file.close()
# print("Your name is", name)

# # Quick Program 2 using "with"
# with open("name.txt", "r") as in_file:
#     name = in_file.read().strip()
# print("Your name is", name)

# # Quick Program 3
# # Note that .strip() is unnecessary since int() handles that whitespace
# in_file = open("numbers.txt", "r")
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# in_file.close()
# print(number1 + number2)

# # Quick Program 3 extended - sum of all numbers
# in_file = open("numbers.txt", "r")
# total = 0
# for line in in_file:
#     number = int(line)
#     total += number
# in_file.close()
# print(total)


# My attempt before pasting solutions

OUTPUT_FILE = 'data.txt'
# user_name = input("What is your name? ")
# out_file = open(OUTPUT_FILE, 'w')
# print(user_name, file=out_file)
# out_file.close()
in_file = open(OUTPUT_FILE)
# file_contents = in_file.read()
file_contents = in_file.readline()
print("Your name is", file_contents)
for line in in_file:
    print(file_contents)
length = len(file_contents)
print(length)
in_file.close()


























