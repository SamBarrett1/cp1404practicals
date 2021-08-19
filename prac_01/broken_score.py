"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Broken program to determine score status
"""


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")


