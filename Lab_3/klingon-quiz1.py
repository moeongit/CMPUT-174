textFile = open("klingon-english.txt", "r")
line1 = textFile.readline()
line2 = textFile.readline()
line3 = textFile.readline()

line3Almost = line3.split("|")[1]
line3Processed = line3Almost.strip("\n")
x = input(f"How do you translate {line3Processed} to Klingon?\n")

if str(x) == str("De'wI'"):
    print("Correct!")
else:
    print("Sorry, the correct answer is De'wI'")