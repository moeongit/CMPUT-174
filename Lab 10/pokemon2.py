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

def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")
main()