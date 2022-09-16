# This program takes two inputs. The x input being what the quote is and the y input being how many times it repeats.

x = input("") # The input to ask the user for the quote
y = int(input("")) # The input to ask the user for how many times he wants the quote to be repeated

for i in range(y): # Used a for loop and range to make this work
    print(x, end = " ") # It will print the quote, and end it with a space so that it is readable
print() # This just removes the % sign from the code.