"""
CP1404 - Prac_02
Samuel Barrett - 13038579
"""


name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# The 'old' manual way to format text with string concatenation:

print("My guitar: " + name + ", first made in " + str(year))


# A better way - using str.format():

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))


# Formatting currency (grouping with comma, 2 decimal places):

print("My {} would cost ${:,.2f}".format(name, cost))


# Aligning columns:

numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:>5}".format(number))


# A version of the above loop using the enumerate function, useful when you want the index and value

for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))


# Things to do

print("Things to do:")
print("{0} {1} for about {2:,.2f}".format(year, name, cost))


# for loop

for i in range(0, 200, 50):
    print("{:>5}".format(i))



