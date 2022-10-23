import random

def make_roll() -> tuple:
    numbers = []
    for i in range(0, 5):
        numbers.append(random.randint(1, 6))
    print(numbers)

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    """
    pass


def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    pass


def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    pass

def main():
    make_roll()
    # TODO: Roll the dice (and print as in demo)
    # TODO: Fill the upper section
    # TODO: Display the upper section


if __name__ == "__main__":
    main()