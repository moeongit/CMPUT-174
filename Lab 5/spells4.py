import random # Imported modules for 
import time

def read_spells(filename: str):
    with open(filename) as file: # Reads the file lines, closes it (with) 
        spells = file.readlines()
    return spells

def get_random_spell(spells: list[str]):
    spell = random.choice(spells).lower() # Takes a random spell from the text file and returns it
    return spell

def display_header(): 
    print("############################################################")
    print("Harry Potter Typing Trainer") # Made 3 lines for a header
    print("############################################################")

def display_instructions():
    with open('instructions.txt', 'r') as filename:
        for line in filename: # Opens the instuctios.txt, reads it, prints the lines
                print(line)

def play_again() -> bool:
    play = input("Would you like to play again? (y/n) ").lower()
    if play == "y": # If the user wants to play, they respond with "y" and we return True, else, we return False
        return True
    elif play == "n":
        return False

def get_user_input(spell: str) -> str:
    start = time.time()
    print(f"Type the following spell: {spell}") 
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    TTT = (len(spell) * 0.3) - 0.3  # Formula for TTT, had to subtract 0.3 because it was adding 0.3 extra seconds
    return TTT  

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    condition = True 
    score = 0 # Set score to 0 so I can implement it
    while condition: # While my condition is True
        spells = read_spells('spells.txt')
        spell = get_random_spell(spells)
        print(spell)
        get_tuple = get_user_input(spell)
        user_input = get_tuple[0] # Had to do this because I couldn't convert the tuples
        user_time = get_tuple[1]
        if user_input.lower() != spell.strip("\n"): # If the user inputs the wrong spell, we take 5 points away 
            score -= 5
            display_feedback(spell, user_input)
            print(f"You lost 5 points! Your score is: {score}")
        elif user_input.lower() == spell.strip("\n"):
            # If the user’s typing time is faster or equal to TTT, the score will be 10.
            if user_time <= get_target_time(spell): # If the user types faster than the goal, we add 10 points
                score += 10
                display_feedback(spell, user_input)
                print(f"You get 10 points! Your score is: {score}")
            # If the user’s typing time is faster or equal to (TTT * 1.5) but slower than TTT, the score will be 6.
            elif get_target_time(spell) < user_time <= (get_target_time(spell) * 1.5):
                score += 6 
                display_feedback(spell, user_input)
                print(f"You get 6 points! Your score is {score}")

            # If the user’s typing time is faster or equal to (TTT * 2) but slower than (TTT * 1.5), the score will be 3. 
            elif (get_target_time(spell) * 1.5) < user_time <= (get_target_time(spell) * 2):
                score += 3
                display_feedback(spell, user_input)
                print(f"You get 3 points! Your score is {score}")

            elif user_time >= get_target_time(spell) * 2: # If the user's typing time is slower than TTT * 2, the score will be 1.
                score += 1
                display_feedback(spell, user_input)
                print(f"You get 1 point! Your score is {score}")
        condition = play_again() # Asks the user to play again after every attempt
    print(f"Your final score is {score}.") # Prints this statement when the user decides to stop playing
    return calculate_points


def display_feedback(spell: str, user_input: str): # Feedback: Tells the user if he is correct or incorrect
    if user_input.lower() != spell.strip("\n"):
        print("Incorrect!")
        print(f"The correct spell was: {spell}")
    else:
        print("Correct!")
    return user_input

def main() -> None: # Called all of these functions
    files = read_spells('spells.txt')  # Reads the text
    random = get_random_spell(files) 
    display_header() # Displays the header
    display_instructions() # Displays the instructions
    calculate_points(str, str, float) # Points with the parameters
    get_target_time(random) # Did this because it was giving an error of converting tuple to string
main()