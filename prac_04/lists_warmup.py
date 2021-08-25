"""Practical 4 - Samuel Barrett - 13038579"""

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 3, 1, 4 (wrong)
numbers[3:4] = 1, 5, 9, 2 (wrong)
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

# Insert 'ten' into the front of the list
numbers.insert(0, 'ten')

# Change the last element of numbers to 1
numbers.append(1)

# Get all the elements from numbers except the first two (slice)
numbers[2:]

# Check if 9 is an element of numbers
9 in numbers[]

