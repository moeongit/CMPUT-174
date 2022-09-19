# This program compares the age of any character of my choice and compares it to 9 characters from the Lord of The Rings. 
# It refactors the last version of my code.
names = [
    "Frodo",
    "Samwise",
    "Gan-dalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
name = input("What is the character's name? ").capitalize() # Asks the user to input a character's name and capitalizes the first letter of the name
age = input("What is the character's age? ") # Asks the user to input a character's age

if name == "": # If the name input has nothing in it, the code will exit
    exit()
if age == "": # If the age input has nothing in it, the code will exit
    exit()

age = int(age) # Converts the age input to an integer
younger = [] # A list for the names of the built-in characters that are younger than the character typed into the input.
older = [] # A list for the names of the built-in characters that are older than the character typed into the input. 

if age < 0:
    print("Invalid age.") # If the user prints an age below 0, the code will print out "Invalid Age".
else:
    for i in range (len(ages)):
        if age < ages[i]:# If the character's age is less than the ages of the characters in the built in list, it will print out the statement below.
            younger.append(names[i]) # If the character is younger, it will add the names he is younger than to a list called "younger"
        elif age > ages[i]:
            older.append(names[i]) # If the character is older, it will add the names he is older than to a list called "older"
    if len(older) != 0: # If the length of the older list isn't 0, print out the statement below.
        print(f"{name} is {age}, and they are older than {', '.join(older)}.") # I used the .join() function to join names of the characters that are older from the "older" list
    if len(younger) != 0: # If the length of the younger list isn't 0, print out the statement below.
        print(f"{name} is {age}, and they are younger than {', '.join(younger)}.") # I used the .join() function to join names of the characters that are younger from the "younger" list