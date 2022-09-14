name = input("Please type your name: ").capitalize()
if name [0] >= "A" and name[0] <= "M":
    side = "left"
else:
    side = "right"
print("" + name + " will be seated on the " + side + " side.")