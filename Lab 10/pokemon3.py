import random

class Pokemon:
    def __init__ (self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health
    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount < self.current_health:
            self.current_health -= amount
        if amount >= self.current_health:
            self.current_health = 0
        if amount < 0:
           self.current_health += amount

    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        # TODO: Implement this method.
        if self.current_health > 0:
            return True
        return False

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        if self.current_health == 0:
            self.current_health = self.max_health

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    pokemon = []
    with open('all_pokemon.txt', 'r') as filename:
        for line in list(filename)[1:]:
            line = line.split("|")
            name = line[0]
            attack = int(line[1])
            defense = int(line[2])
            max_health = int(line[3])
            pokemon.append(Pokemon(name, attack, defense, max_health, max_health))
    return pokemon

def main():
    """
    Battle of two Pokemon
    """
    mons = read_pokemon_from_file("all_pokemon.txt")
    pokemon = random.sample(mons, 2)
    print(f"Welcome, {pokemon[0]} and {pokemon[1]}!")

main()