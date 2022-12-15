import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def get_rank_value(self):
        rank_value = {'A':1, 'X':10, 'J':11, 'Q':12, 'K':13}
        if self.rank in rank_value:
            return rank_value[self.rank]
        else:
            return int(self.rank)
class Deck:
    def __init__(self):
        self.deck = []
        suits = ['H', 'D', 'S', 'C']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
    def __str__(self):
        display_str = ''
        for card in self.deck:
            display_str += f"{card}\n"
        return display_str
class Hand:
    def __init__(self):
        self.players_hand = []
    def add(self, card):
        self.players_hand.append(card)
    def get_length(self):
        return len(self.players_hand)
    def get_hand(self):
        return self.players_hand
    def __str__(self):
        display_str = f'{"+---"* self.get_length()}+\n'
        display_str += "|"
        for card in self.players_hand:
            display_str += f" {card.get_rank()} |"
        display_str += "\n"
        display_str = "|"
        for card in self.players_hand:
            display_str += f' {card.get_suit()} |'
        display_str += '\n'
        display_str += f'{"+---"* self.get_length()}+\n'
        return display_str

def main():
    #card = Card('D','3')
    #print(card)  # __str__ method is called
    #print(card.get_rank_value())
    deck = Deck()
    deck.shuffle()
    #print(deck) # __str__ method in the Deck class is called
    #for i in range(5):
    #    card = deck.deal()  # card is an instance of the Card class
    #    print(card)
    hand = Hand()
    for i in range(8):
        hand.add(deck.deal())
    print(hand) # __str__ in the Hand class will be called
if __name__ == '__main__':
    main()

