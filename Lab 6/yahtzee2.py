import random

def make_roll() -> tuple:
    numbers = []
    for i in range(0, 5):
        numbers.append(random.randint(1, 6))
    numbers = tuple(numbers)
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
    print("Upper Section: ")
    print(f"Aces: {upper_section_scores[0]}")
    print(f"Twos: {upper_section_scores[1]}")
    print(f"Threes: {upper_section_scores[2]}")
    print(f"Fours: {upper_section_scores[3]}")
    print(f"Fives: {upper_section_scores[4]}")
    print(f"Sixes: {upper_section_scores[5]}")

def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    for i in roll:
        if roll.count(i) == number:
            return sum(roll)

    return 0

def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    for number in roll:
        if number != roll[0]:
            return 0

    return 50

def main():
    roll = make_roll()
    upper = fill_upper_section(roll)
    display_upper_section(upper)
    print("Lower section: ")
    print(f"Three of a kind: {num_of_a_kind(roll, 3)}")
    print(f"Four of a kind: {num_of_a_kind(roll, 4)}")
    print(f"Yahtzee: {yahtzee(roll)}")


if __name__ == "__main__":
    main()