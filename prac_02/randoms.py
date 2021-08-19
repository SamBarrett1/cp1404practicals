"""
CP1404 - Prac_02
Samuel Barrett - 13038579
"""

# 1. 10 was seen first, the smallest 5 and the largest 20
# 2. 5 was seen, the smallest was 3 the largest 9
# 3. 2.904157541622413 was seen the smallest could have been 2.5 the largest 5.5

import random  # normally placed at the top of the file

# code to produce a random number inclusive of 1 and 100
print(random.randint(1, 100))

# testing multiple runs to see inclusive 1 and 100
for i in range(0, 10):
    print(random.randint(1, 100), end=" ")

