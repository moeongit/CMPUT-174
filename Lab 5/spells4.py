import random
import time

def read_spells(filename: str):
    with open(filename) as file:
        spells = file.readlines()
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
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    TTT = (len(spell) * 0.3) - 0.3
    return TTT  

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    condition = True
    score = 0
    while condition:
        spells = read_spells('spells.txt')
        spell = get_random_spell(spells)
        print(spell)
        get_tuple = get_user_input(spell)
        user_input = get_tuple[0]
        user_time = get_tuple[1]
        if user_input.lower() != spell.strip("\n"):
            score -= 5
            display_feedback(spell, user_input)
            print(f"You lost 5 points! Your score is: {score}")
        elif user_input.lower() == spell.strip("\n"):
            if user_time <= get_target_time(spell):
                score += 10
                display_feedback(spell, user_input)
                print(f"You get 10 points! Your score is: {score}")
        elif user_input.lower() == spell.strip("\n"):
            if get_target_time(spell) < user_time <= (get_target_time(spell) * 1.5):
                score += 6
                display_feedback(spell, user_input)
                print(f"You get 6 points! Your score is {score}")
        elif user_input.lower() == spell.strip("\n"):
            if user_time >= get_target_time(spell) * 2:
                score += 1
                display_feedback(spell, user_input)
                print(f"You get 1 point! Your score is {score}")

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
    sum = read_spells('spells.txt')
    random = get_random_spell(sum)
    display_header()
    display_instructions()
    calculate_points(str, str, float)
    get_target_time(random)
main()