# This program takes the name and age of a character and compares it to Frodo and Gollum's age.
frodo_age = 51
gollum_age = 589
name = input("What is the character's name? ").capitalize() # Asks the user for a character name and capitalizes the first letter of that name.
age = int(input("What is the character's age? ")) # Asks the user for an integer of the character's age.
if age < 0:
    print("Please type a positive number.") # If the age is less than 0, the program asks the user to type a positive number".
younger_older = ""
if age > frodo_age and gollum_age: 
    print(f"{name} is {age} years old, and they are older than Gollum and Frodo.") # If the character's age is greater than Frodo's and Gollum's, it will print that out.
elif frodo_age < age < gollum_age:
    print(f"{name} is {age} years old, and they are older than Frodo but younger than Gollum.") #  If the character's age is greater than Frodo's but less than Gollum's, it will print that out.
elif age < frodo_age and gollum_age:
    print(f"{name} is {age} years old, and they are younger than Frodo and Gollum.") # If the character's age is less than Frodo's and Gollum's, it will print that out.