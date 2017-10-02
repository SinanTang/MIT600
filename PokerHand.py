from TP_CH18 import Hand, Deck


class Hist(dict):
    def __init__(self, seq=[]):
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        self[x] = self.get(x, 0) + f
        if self[x] == 0: del self[x]



class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush', 'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
        self.suits = Hist()
        self.ranks = Hist()

        for c in self.cards:
            self.suits.count(c.suit)
            self.suits.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def same_rank(self, card_num=2, pair_num=1):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= card_num:
                count += 1
        if count >= pair_num:
            return True
        else:
            return False

    def same_rank_exact(self, card_num=2):
        self.rank_hist()
        for val in self.ranks.values():
            if val == card_num: return True
        return False

    def has_pair(self):
        return self.same_rank(2,1)

    def has_twopair(self):
        return self.same_rank(2,2)

    def has_three_of_a_kind(self):
        return self.same_rank(3, 1)

    def has_four_of_a_kind(self):
        return self.same_rank(4, 1)

    def has_full_house(self):
        return self.same_rank_exact(3) and self.same_rank_exact(2)

    def has_straight0(self):
        self.rank_hist()
        key_ls = list(self.ranks.keys())
        key_ls.sort()
        # print(key_ls)
        for i in range(len(key_ls)-4):
            if key_ls[i] == key_ls[i+4] - 4:
                # print(i)
                return True
        # when ace is the highest
        if key_ls[0] == 1 and key_ls[-4] == 10: return True
        return False

    def has_straight(self):
        ranks = self.ranks.copy()
        print('In has_straight, ranks:', ranks) # empty {}
        ranks[14] = ranks.get(1, 0)
        return self.in_a_row(ranks, 5)

    def in_a_row(self, ranks, n=5):
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else: count = 0
        return False

    def has_straight_flush0(self):
        card_tuple_ls = []
        for card in self.cards:
            card_tuple_ls.append((card.rank, card.suit))
        card_tuple_ls.sort()
        print(card_tuple_ls)

        for i in range(len(card_tuple_ls)-4):
            if (card_tuple_ls[i][0] == card_tuple_ls[i+4][0]-4) and \
                    (card_tuple_ls[i][1] == card_tuple_ls[i+4][1]):
                # print(card_tuple_ls[i])
                return True
        # if card_tuple_ls[]
        return False

    def has_straightflush(self):
        # partition the hand by suit and check each sub-hand for a straight
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)
        # print(d.values())

        # to see if any of the partitioned hands has a straight
        for hand in d.values():
            print(hand, '\n')
            if len(hand.cards) < 3:
                continue
            hand.make_histograms()
            if hand.has_straight():
                return True
        return False



if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(1):
    # range_number * num of cards in a hand <= 53 cards..
        hand = PokerHand()
        deck.move_cards(hand, 10)
        hand.sort()
        print(hand)
        print()
        # print('Flush:', hand.has_flush())
        # print('Pair:', hand.has_pair())
        # print('Two Pair:', hand.has_twopair())
        # print('Three of a kind:', hand.has_three_of_a_kind())
        # print('Four of a kind:', hand.has_four_of_a_kind())
        # print('Full House:', hand.has_full_house())
        print('Straight:', hand.has_straight())
        print('Straight Flush:', hand.has_straightflush())
        print()
        print()