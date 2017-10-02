### Think Python2 CH18 Inheritance ###

import random
from functools import total_ordering

@total_ordering
class Card:
    """Represents a standard playing card"""
    def __init__(self, suit=0, rank=2):
        # instance attributes
        self.suit = suit
        self.rank = rank
    # class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5','6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        # # check the suits
        # if self.suit < other.suit: return True
        # if self.suit > other.suit: return False
        #
        # # suits are the same... check ranks
        # return self.rank < other.rank

        # or use tuple comparison
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


queen_of_diamonds = Card(1, 12)
# print(queen_of_diamonds)

# print(queen_of_diamonds.rank_names)
# print(Card.rank_names)
# print(type(Card), type(queen_of_diamonds))
# <class 'type'> <class '__main__.Card'>


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def add_card(self, card):
        # a veneer
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        # sorts ascendingly
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    # def deal_hands(self, num_hand=1, num_cards=1):
    #     hands = []
    #     changing_cards = self.cards
    #     print(str(self.cards))
    #     print(len(changing_cards),'\n')
    #     for i in range(num_hand):
    #         hand = Deck()
    #         hand.cards = []
    #         hand.cards = random.choices(changing_cards, k=num_cards)
    #         hands.append(hand)
    #         print(len(changing_cards))
    #         changing_cards = [i for i in changing_cards if i not in hand.cards]
    #         print(len(changing_cards), '\n')
    #
    #     return hands



deck = Deck()
# hands = deck.deal_hands(4, 13)

# for i in hands:
#     print('hand dealt:')
#     print(i, '\n')

# print(deck)
#
# print()
#
# deck.pop_card()
# print(deck)
#
# print()
#
# deck.shuffle()
# print(deck)
#
# print()
#
# deck.sort()
# print(deck)


class Hand(Deck):
    """represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label



hand = Hand('new hand')
# print(hand.cards, hand.label)

card = deck.pop_card()

hand.add_card(card)
# print(hand)
# print()

deck.move_cards(hand, 3)

# print(hand, '\n', deck)


def find_defining_class(obj, method_name):
    for ty in type(obj).mro():
        print(ty.__dict__)
        if method_name in ty.__dict__:
            return ty

# find_defining_class(hand, 'shuffle')



## Exercise 18.1 - draw class diagram
class PingPongParent:
    pass

class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong

class Pong(PingPongParent):
    def __init__(self, pings = None):
        if pings is None:
            self.pings = []
        else:
            self.pings = pings
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)


## Exercise 18.2 - write a Deck method deal_hands


## Exercise 18.3 - estimate the probability of drawing various hands