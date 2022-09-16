# This program takes the name and age of a character and compares it to Frodo and his age. 
# If they are younger, it will print out that they are younger than Frodo. The same goes for if they are older/the same age.
name = input("What is the character's name? ").capitalize() # Asks the user to input a name, the capitalize function always capitalizes the first letter of the word.
age = int(input("What is the character's age? ")) # Asks the user to input an age.
frodo_age = 51 # Frodo's age is 51 so I used that to compare it to the character's ages.
if age < 0:
    print("Please type a positive number.") # If a user types an integer less than 0, it will tell them to print a positive number.
younger_older = "" 
if str(age) > str(frodo_age):
    younger_older = "older" # If they are older, the function will be "older".
else:
    younger_older = "younger" # Or if they are younger, the function will be "younger".
if str(age) == str(frodo_age):
    younger_older = "same age" # If the character is the same age as Frodo, it will print out that they are the same age.
    print(f"{name} is {age} years old, and they are of the same age as Frodo.") # I had to make 2 print statements because they could be the same age as Frodo.
else:
    print(f"{name} is {age} years old, and they are {younger_older} than Frodo.")
