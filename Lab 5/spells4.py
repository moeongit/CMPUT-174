import random
import time

def read_spells(filename: str):
    with open('spells.txt') as filename:
        spells = filename.readlines()
    return spells

def get_random_spell(spells: list[str]):
    spell = random.choice(spells).lower()
    return spell

def display_header():
    print("############################################################")
    print("Harry Potter Typing Trainer")
    print("############################################################")

def display_instructions():
    with open('instructions.txt', 'r') as filename:
        for line in filename:
                print(line)

def play_again() -> bool:
    play = input("Would you like to play again? (y/n) ").lower()
    if play == "y":
        return True
    elif play == "n":
        return False

def get_user_input(spell: str) -> str:
    #start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    #user_time = round(time.time() - start, 2)
    #print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input

def get_target_time(spell: str) -> float:
    pass

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    condition = True
    score = 0
    while condition:
        spells = read_spells('spells.txt')
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        if user_input.lower() != spell.strip("\n"):
            score -= 5
            display_feedback(spell, user_input)
            print(f"You lost 5 points! Your score is: {score}")
        else:
            score += 10
            display_feedback(spell, user_input)
            print(f"You get 10 points! Your score is: {score}")
        condition = play_again()
    print(f"Your final score is {score}.")


def display_feedback(spell: str, user_input: str):
    if user_input.lower() != spell.strip("\n"):
        print("Incorrect!")
        print(f"The correct spell was: {spell}")
    else:
        print("Correct!")
    return user_input

def main() -> None:
    display_header()
    display_instructions()
    calculate_points(str, str, float)
    
main()