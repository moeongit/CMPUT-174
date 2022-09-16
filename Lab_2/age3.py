# This program takes a character's name and age and compares it to the age's of Pippin, Frodo, Gollum, Arwen.
pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901
name = input("What is the character's name? ").capitalize() # Asks the user for a character name and capitalizes the first letter of that name.
age = int(input("What is the character's age? ")) # Asks the user for an integer of the character's age.
if age < 0:
    print("Invalid age.") # If the age is negative, it will tell the user that it is an invalid age.
else: # If the user prints a valid age greater than 0, these functions will work, if they match the criteria.
    if age < pippin_age:
        print(f"{name} is {age} years old, and they are younger than Arwen, Gollum, Frodo, Pippin.") # If the character's age is less than Pippin's age, it will print out a statement confirming this, and it will say that they are younger than everyone else.
    elif age > arwen_age:
        print(f"{name} is {age} years old, and they are older than Arwen, Gollum, Frodo, Pippin.") #  If the character's age is greater than Arwen's age, it will print out a statement confirming this, and it will say that they are older than everyone else.
    elif pippin_age < age < frodo_age:
        print(f"{name} is {age} years old, and they are older than Pippin.") # If the character's age is greater than Pippin's but less than Frodo's, it will print out a 2 statements, one for who the character is older than and the other for who they are younger than.
        print(f"{name} is {age} years old, and they are younger than Arwen, Gollum, Frodo.") 
    elif frodo_age < age < gollum_age:
        print(f"{name} is {age} years old, and they are older than Frodo, Pippin.") # If the character's age is greater than Frodo's but less than Gollum's, it will print out a 2 statements, one for who the character is older than and the other for who they are younger than.
        print(f"{name} is {age} years old, and they are younger than Arwen, Gollum.")
    elif gollum_age < age < arwen_age:
        print(f"{name} is {age} years old, and they are older than Gollum, Frodo, Pippin.") # If the character's age is greater than Gollum's but less than Frodo's, it will print out a 2 statements, one for who the character is older than and the other for who they are younger than.
        print(f"{name} is {age} years old, and they are younger than Arwen.")
    elif age == pippin_age:
        print(f"{name} is {age} years old, and they are of the same age as Pippin.") # If the character's age is equal to Pippin's, it will print out 2 statements, one saying that they are of the same age, and the other saying who they are younger than, because they can't be older than anyone since Pippen is the youngest.
        print(f"{name} is {age} years old, and they are younger than Arwen, Gollum, Frodo.")
    elif age == frodo_age:
        print(f"{name} is {age} years old, and they are of the same as as Frodo.") # If the character's age is equal to Frodo's, it will print out 3 statements, one saying that they are of the same age, and the 2nd one saying who they are older than, and the 3rd saying who they are younger than.
        print(f"{name} is {age} years old, and they are older than Pippin.")
        print(f"{name} is {age} years old, and they are younger than Arwen, Gollum.")
    elif age == gollum_age:
        print(f"{name} is {age} years old, and they are of the same age as Gollum.") # If the character's age is equal to Gollum's, it will print out 3 statements, one saying that they are of the same age, and the 2nd one saying who they are older than, and the 3rd saying who they are younger than.
        print(f"{name} is {age} years old, and they are older than Frodo, Pippin.")
        print(f"{name} is {age} years old, and they are younger than Arwen.")
    elif age == arwen_age:
        print(f"{name} is {age} years old, and they are of the same age as Arwen.") # If the character's age is equal to Arwen's, it will print out 2 statements, one saying that they are of the same age, and the other saying that they are older than everyone else since Arwen is the oldest.
        print(f"{name} is {age} years old, and they are older than Gollum, Frodo, Pippin.")

        # All of these elif statements are similar as there are multiple different outcomes when comparing one person's age to 4 people.