# This program asks the user to translate an English word to Klingon.
# The user must pick a consonant from the list to practice with.
# If the word the user enters is incorrect, the user will have 2 hints.
# If the word is still incorrect, the program will print out the correct word.

import random

textFile = open("klingon-english.txt", "r") # Opened the text file, "r" is to read it
line = textFile.readlines() # Read the lines of the file
textFile.close() 

i = 0 # Counter

for letter in line:
    line[i] = letter.strip("\n") # This goes through every line of the text and strips the "\n"
    i += 1

user_choose = input("Which consonant would you like to practice with? ")

consonants = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y", "'"] # All the consonants the user could practice from
klingon_word = "" # Made 2 lists for the words translated in the different languages
enlish_word = ""

while user_choose not in consonants: # If the consonant the user entered isnt apart of the list, the input will repeat
    user_choose = input("Which consonant would you like to practice with? ")
length = len(user_choose)
for word in line:
    if user_choose in word[0:length]:
        index = word.find("|") # Found the vertical bar, and the english word was 1 after the index, while the klingon word was opposite
        english_word = word[index+1:]
        klingon_word = word[0:index]

turns_taken = 0 # Counter for the turns the user has taken to translate the word

user_answer = input(f"How do you translate {english_word.capitalize()} to Klingon? ")

random_number = random.randint(1, len(klingon_word) - 2) # Made a function to show the second character of the word as well as the second last character

if user_answer == klingon_word:
    print("Correct!")
else:
    if user_answer != klingon_word:
        turns_taken += 1
        while turns_taken <= 2: # While the turns the user has taken is less than 3, all of the below will occur
            if turns_taken == 1:
                print("Incorrect. Take a hint: " + klingon_word[0] + '*'*(len(klingon_word) - 2) + klingon_word[len(klingon_word)-1])
            elif turns_taken == 2:
                print("Incorrect. Take another hint: ", end= '')
                print(klingon_word[0], end = '')
                print('*'*(len(klingon_word[1:random_number])), end = '')
                print(klingon_word[random_number],end='')
                print('*'*(len(klingon_word[random_number+1:len(klingon_word)-1])), end = '')
                print(klingon_word[len(klingon_word)-1])
            user_answer = input(f"How do you translate {english_word.capitalize()} to Klingon? ")
            if user_answer != klingon_word:
                turns_taken += 1
                if turns_taken == 3:
                    print(f"Incorrect. The correct answer is {klingon_word.capitalize()}.")