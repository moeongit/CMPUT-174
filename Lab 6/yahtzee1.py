import random

def make_roll() -> tuple:
    numbers = []
    for i in range(0, 5):
        numbers.append(random.randint(1, 6))
    print(f"Rolling the dice. . . {numbers}")
    return numbers

def sum_of_given_number(roll: tuple, number: int) -> int:
    count = 0
    for i in range(len(roll)):
        if number == roll[i]:
            count += 1
    sum = count * number
    return sum

def fill_upper_section(roll: tuple) -> list:
    upper = []
    for i in range(1, 7):
        upper.append(sum_of_given_number(roll, i))
    return upper

def display_upper_section(upper_section_scores: list) -> None:
    print(f"Aces: {upper_section_scores[0]}")
    print(f"Twos: {upper_section_scores[1]}")
    print(f"Threes: {upper_section_scores[2]}")
    print(f"Fours: {upper_section_scores[3]}")
    print(f"Fives: {upper_section_scores[4]}")
    print(f"Sixes: {upper_section_scores[5]}")

def main():
    roll = make_roll()
    upper = fill_upper_section(roll)
    display_upper_section(upper)

if __name__ == "__main__":
    main()