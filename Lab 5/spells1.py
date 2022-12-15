import random

def read_spells(filename: str):
    with open('spells.txt') as filename:
        spells = filename.readlines()
    return spells

def get_random_spell(spells: list[str]):
    spell = random.choice(spells).lower()
    return spell

def main():
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)
main()