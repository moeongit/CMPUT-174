import random

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

def get_user_input(spell: str) -> str:
    user_input = input(f"Type the following spell: {spell}")
    return user_input

def display_feedback(spell: str, user_input: str):
    if user_input != spell.strip("\n"):
        print("Incorrect!")
        print(f"The correct spell was: {spell}")
    else:
        print("Correct!")
    return user_input

def main() -> None:
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)
main()