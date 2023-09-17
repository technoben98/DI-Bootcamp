import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        if len(self.cards) == 52:
            print("There are 52 cards in deck!")
            random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) != 0:
            print(f"Your card {self.cards[0].suit} {self.cards[0].value}")
            return self.cards.pop(0)
        else:
            print("Deck is empty.")

deck1 = Deck()
deck1.shuffle()

deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
print(len(deck1.cards))
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
print(len(deck1.cards))
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
print(len(deck1.cards))
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
print(len(deck1.cards))
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
deck1.deal()
print(len(deck1.cards))
deck1.deal()
print(len(deck1.cards))