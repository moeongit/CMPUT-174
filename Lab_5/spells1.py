import random

def read_spells(filename: str):
    textFile = open('spells.txt', 'r')
    lines = textFile.readlines()
    textFile.close()
    return lines

def get_random_spell(spells: list[str]):
    lines = open('spells.txt').read().splitlines()
    return random.choice(lines).lower(  )
 
def main():
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)
main()

