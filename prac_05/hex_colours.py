COLOR_NAME = {"aliceblue": "#f0f8ff", "amber": "#ffbf00", "aqua": "#00ffff", "ashgrey": "#b2beb5", "bronze": "#cd7f32",
              "cadetblue": "#5f9ea0", "celeste": "#b2ffff"}
user_input = input("Enter color: ").lower()
while user_input != "":
    try:
        print(f"The color code is {COLOR_NAME[user_input]}")
    except KeyError:
        print("Color not found!")

    user_input = input("Enter color: ").lower()
