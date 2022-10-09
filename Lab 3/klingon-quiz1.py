# This program translates the word "Computer" in English to Klingon. It opens the text file with words translated to and from English and Klingon and reads it
textFile = open("klingon-english.txt", "r") # Opened the text file, "r" is to read it
line1 = textFile.readline() # We wanted line 3 so i read everyline up until line 3
line2 = textFile.readline()
line3 = textFile.readline()
textFile.close()
line3Almost = line3.split("|")[1] # This takes line 3, splits the vertical bar (|) and the [1] takes the first index after the bar, which is computer
line3Processed = line3Almost.strip("\n") # This takes out the "\n" in line 3
user_translate = input(f"How do you translate {line3Processed} to Klingon?\n")

if str(user_translate) == str("De'wI'"):
    print("Correct!")
else:
    print("Sorry, the correct answer is De'wI'")