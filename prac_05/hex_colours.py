"""
Practical 5 - Samuel Barrett - 13038579
Hex colour program
"""


HEX_COLOUR_DICT = {"AliceBlue": "#f0f8ff", "Blue": "#0000ff", "Green": "#008000", "Yellow": "#ffff00",
                   "Red": "#ff0000", "Grey": "#808080", "Purple": "#800080", "Violet": "#ee82ee", "Orange": "#ffa500"}

print(HEX_COLOUR_DICT)

state_color = input("What colour in hex: ")
while state_color != "":
    if state_color in HEX_COLOUR_DICT:
        print("{} is {}".format(state_color, HEX_COLOUR_DICT[state_color]))
    else:
        print("Invalid colour")
    state_color = input("What colour in hex: ")
