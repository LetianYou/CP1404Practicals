COLOUR_NAME = {"absolute zero": "#0048ba", "aliceblue": "#f0f8ff", "acid green": "#b0bf1a",
               "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
               "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}

colour_code = input("Enter the colour name and the colour code will be show: ").lower()
while colour_code != "":
    if colour_code in COLOUR_NAME:
        print(COLOUR_NAME[colour_code])
    else:
        print("Invalid colour name")
    colour_code = input("Enter the colour name and the colour code will be show: ").lower()
