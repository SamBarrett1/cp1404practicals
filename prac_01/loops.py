"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Loops
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()


for i in range(0, 101, 10):
    print(i, end=' ')
print()


for i in range(20, 0, -1):
    print(i, end=' ')
print()


star_total = int(input("How many stars: "))
for i in range(star_total):
    print('*', end=' ')
print()


star_total = int(input("How many stars: "))
for i in range(star_total + 1):
    print('*' * i)
print()

