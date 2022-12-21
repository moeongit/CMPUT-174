'''
Version 1 - implment the Card,Deck and Hand class and test these classes
Version 2 - Add a Poker class - check_straight,check_flush,check_straight_flush
Version 3 - get_rank_frequency, check_four_of_a_kind, check_three_of_a_kind, full_house, check_two_pair, check_one_pair
Version4 - check_hand - return points
'''

import random
class Poker:
    def __init__(self,player_hand):
        self.player_hand = player_hand
    def get_rank_frequency(self)->dict:
        ''' returns how many times a rank occurs in a player's hand'''
        rank_frequency = {}
        for card in self.player_hand.get_hand():
            rank_frequency[card.get_rank()] = rank_frequency.get(card.get_rank(),0) + 1 
        return rank_frequency    
    def check_two_pair(self):
        '''check if the hand has 2 cards of one rank, 2 cards of a another rank and a 3rd card of another rank'''
        ranks_d = self.get_rank_frequency()
        # ranks_d = {5:2, 7:2, 3:1}
        # ranks_d.values --> 2,2,1--->[2,2,1]
        rank_list = list(ranks_d.values())
        # Apply the count method in the list class
        return rank_list.count(2) == 2 and rank_list.count(1) == 1
    
    
    def check_one_pair(self):
        '''check if the hand has 2 cards of one rank, 3 cards of 3 other ranks'''
        ranks_d = {}
        ranks_d = self.get_rank_frequency()
        # ranks_d = {5:2, 7:2, 3:1}
        # ranks_d.values --> 2,2,1--->[2,2,1]
        rank_list = list(ranks_d.values())
        # Apply the count method in the list class
        return rank_list.count(2) == 1 and rank_list.count(1) == 3
        
    def check_four_of_a_kind(self):
        '''checks if the hand has 4 cards of one rank and 1 card of another rank'''
        ranks_d = self.get_rank_frequency()
        # ranks_d = [5:4, 2:1] -> ranks_d.values() ---> 4,1
        return 4 in ranks_d.values() and 1 in ranks_d.values()
    
    def check_three_of_a_kind(self):
        '''checks if the hand has 3 cards of one ranks and 2 cards of 2 other ranks'''
        ranks_d = self.get_rank_frequency()
    
        return 3 in ranks_d.values() and not 2 in ranks_d.values()        
    
    def check_full_house(self):
        '''checks if the hand has 3 cards of one rank and 2 cards of another rank'''
        ranks_d = self.get_rank_frequency()
    
        return 3 in ranks_d.values() and 2 in ranks_d.values()        
    
    def check_straight(self):
        '''checks if cards are of sequential ranks or not'''
        ranks = []
        for card in self.player_hand.get_hand(): # returns a list of cards ***IMPORTANT
            value = card.get_rank_value()
            ranks.append(value)
        ranks.sort() # sorts the list in place in ascending order
        return ranks == list(range(min(ranks),max(ranks) + 1))
    def check_flush(self):
        '''checks if all cards are of the same suit'''
        suits_d = {}
        for card in self.player_hand.get_hand():
            suit = card.get_suit()
            suits_d[suit] = suits_d.get(suit,0) + 1
        # Method in Dictionary class - get, items, keys, values
        return 5 in suits_d.values()
    def check_straight_flush(self):
        return self.check_straight() and self.check_flush()
    def check_hand(self)->int:
        '''checks player_hand and returns the points'''
        if self.check_straight_flush():
            print('Straight Flush')
            return 1000
        elif self.check_four_of_a_kind():
            print('Four of a Kind')
            return 800
        elif self.check_full_house():
            print('Full House')
            return 600
        elif self.check_flush():
            print('Flush')
            return 500
        elif self.check_straight():
            print('Straight')
            return 400
        elif self.check_three_of_a_kind():
            print('Three of a kind')
            return 300
        elif self.check_two_pair():
            print('Two Pair')
            return 100
        elif self.check_one_pair():
            print('One Pair')
            return 50
        else:
            return 0      
class Card:
    def __init__(self,suit:str,rank:str):
        self.suit = suit
        self.rank = rank
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def __str__(self):
        return self.rank+' of ' +self.suit
    def get_rank_value(self)->int:
        rank_value = {'A':1,'X':10,'J':11,'Q':12,'K':13}
        if self.rank in rank_value: # checking if the key is in the dictionary
            return rank_value[self.rank] # self.rank is the key that we use to index into the dictionary
        else:
            return int(self.rank)
class Deck:
    def __init__(self):
        self.deck = []
        suits = ['H','D','S','C']
        ranks = ['A','2','3','4','5','6','7','8','9','X','J','Q','K']
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
    def __str__(self):
        display_str = ''
        for card in self.deck:
            display_str += f'{card}\n'
        return display_str
class Hand:
    # representing a player's hand
    def __init__(self):
        self.player_hand = []
    def add(self,card):
        self.player_hand.append(card)
    def get_length(self):
        return len(self.player_hand)
    def get_hand(self):
        return self.player_hand
    def __str__(self):
        display_str =f'{"+---"* self.get_length()}+\n'
        # Start printing the ranks 
        display_str += '|'
        for card in self.player_hand:
            display_str += f' {card.get_rank()} |'
        display_str +='\n'
        # Start printing the suits
        display_str += '|'
        for card in self.player_hand:
            display_str += f' {card.get_suit()} |'
        display_str += '\n'
        display_str += f'{"+---"* self.get_length()}+\n'
        return display_str
def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand()
    for i in range(5):
        hand.add(deck.deal())
    print(hand)
    poker = Poker(hand)
    print(poker.check_hand())
if __name__ == "__main__":
    main()