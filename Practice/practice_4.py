# Exercise_name = input("What is the name of your exercise? ")
# sets = int(input("How many sets are you doing? "))
# reps = int(input("How many reps are you doing? "))
# seconds = int(input("How many seconds are you resting for? "))

# print("Perfrom" , (sets) , "sets of " + Exercise_name + " at" , (reps) , "reps each. Rest for" , (seconds) , "secs between each set.")




Exercise = input("Format: ")

sets = Exercise[0:1]
reps = Exercise[2:3]
time = Exercise[4: ]


print(sets, reps, time)

'''
5x4, 45 secs
first character from the string for sets
right of x, second character for reps
right side of, read the number, for time

'''







