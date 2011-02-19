#~ * High Card: Highest value card.
#~ * One Pair: Two cards of the same value.
#~ * Two Pairs: Two different pairs.
#~ * Three of a Kind: Three cards of the same value.
#~ * Straight: All cards are consecutive values.
#~ * Flush: All cards of the same suit.
#~ * Full House: Three of a kind and a pair.
#~ * Four of a Kind: Four cards of the same value.
#~ * Straight Flush: All cards are consecutive values of same suit.
#~ * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

#~ The cards are valued in the order:
#~ 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#~ Club
#~ Spade
#~ Heard
#~ Diamonds

import copy

card_values = "23456789TJQKA"
color_values = "CSHD"

def find_pair(hand):
    """ Find the next pair in the hand

        >>> find_pair(['5C', '5S', '3C', '3S', '7H'])
        (('5C', '5S'), ['3C', '3S', '7H'])
        >>> find_pair(['3C', '3S', '7H'])
        (('3C', '3S'), ['7H'])
        >>> find_pair(['7H'])
        (None, ['7H'])

        >>> find_pair(['5C', '3C', '3S', '7H', '5S'])
        (('5C', '5S'), ['3C', '3S', '7H'])
    """
    hand = copy.copy(hand)
    for a in range(len(hand)):
        for b in range(a + 1, len(hand)):
            if hand[a][0] == hand[b][0]:
                #~ pair = (a, b)
                first_card = hand[a]
                second_card = hand[b]
                hand.remove(first_card)
                hand.remove(second_card)
                return ((first_card, second_card), hand)

    return (None, hand)

class ResultBase():
    """
        Comparism via Rank does work:
        >>> ResultBase(ResultBase.ROYAL_FLUSH) > ResultBase(ResultBase.HIGH_CARD)
        True

        >>> ResultBase(ResultBase.HIGH_CARD) < ResultBase(ResultBase.ROYAL_FLUSH)
        True
    """
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __init__(self, rank):
        self.rank = rank

    def __cmp__(self, other):
        if self.rank == other.rank:
            return self.__cmp_rank__(other)
        else:
            return cmp(self.rank, other.rank)

    def __cmp_rank__(self, other):
        raise Exception("not implemented")


def cmp_cards_color(a, b):
    if card_values.find(a[0]) == card_values.find(b[0]):
        return cmp(color_values.find(a[1]), color_values.find(b[1]))

    return cmp(card_values.find(a[0]), card_values.find(b[0]))

def cmp_cards(a, b):
    return cmp(card_values.find(a[0]), card_values.find(b[0]))


class OnePairResult(ResultBase):
    def __init__(self, pair, kickers):
        ResultBase.__init__(self, ResultBase.ONE_PAIR)
        self.pair = pair
        self.kickers = sorted(kickers, cmp_cards_color)
        self.kickers.reverse()

    def __repr__(self):
        """
            >>> OnePairResult(('5C', '5S'), ['3S', '3C', '7H'])
            OnePairResult(('5C', '5S'), ['7H', '3S', '3C'])
        """
        return "OnePairResult(%s, %s)" % (self.pair, self.kickers)


    def __cmp_rank__(self, other):
        """
            >>> first = OnePairResult(('5C', '5S'), ['3C', '3S', '7H'])
            >>> first > OnePairResult(('4C', '4S'), ['3C', '3S', '7H'])
            True
            >>> first < OnePairResult(('6C', '6S'), ['3C', '3S', '7H'])
            True

            >>> first > OnePairResult(('5C', '5S'), ['3C', '3S', '2H'])
            True
            >>> first == OnePairResult(('5C', '5S'), ['3C', '3S', '7H'])
            True

        """
        if self.pair[0][0] > other.pair[0][0]:
            return 1
        elif self.pair[0][0] < other.pair[0][0]:
            return -1
        else:
            for pair in zip(self.kickers, other.kickers):
                r = cmp_cards(pair[0], pair[1])
                if r == 0:
                    continue
                return r

            return 0

        raise Exception("not implemented")

class TwoPairResult(ResultBase):
    def __init__(self, first_pair, second_pair, kicker):
        ResultBase.__init__(self, ResultBase.TWO_PAIRS)
        self.first_pair = first_pair
        self.second_pair = second_pair
        self.kicker = kicker

    def __repr__(self):
        """
            >>> TwoPairResult(('5C', '5S'), ('3C', '3S'), '7H')
            TwoPairResult(('5C', '5S'), ('3C', '3S'), '7H')
        """
        return "TwoPairResult(%s, %s, '%s')" % (self.first_pair, self.second_pair, self.kicker)

    def __cmp_rank__(self, other):
        """
            >>> first_hand = TwoPairResult(('5C', '5S'), ('3C', '3S'), '7H')
            >>> second_hand = TwoPairResult(('5C', '5S'), ('3C', '3S'), '7D')

            >>> first_hand == second_hand
            True

            >>> first_hand > TwoPairResult(('5C', '5S'), ('2C', '2S'), '7D')
            True

            >>> first_hand < TwoPairResult(('5C', '5S'), ('8C', '8S'), '7D')
            True

            >>> first_hand > TwoPairResult(('2C', '2S'), ('8C', '8S'), '7D')
            True

            >>> first_hand < TwoPairResult(('6C', '6S'), ('8C', '8S'), '7D')
            True
        """
        if self.first_pair[0][0] == other.first_pair[0][0]:
            if self.second_pair[0][0] == other.second_pair[0][0]:
                if self.kicker[0] == other.kicker[0]:
                    return 0
            elif self.second_pair[0][0] > other.second_pair[0][0]:
                return 1
            else:
                return -1
        elif self.first_pair[0][0] >= other.first_pair[0][0]:
            return 1
        else:
            return -1

        raise Exception("not implemented")


def is_two_pair(hand):
    """ return the two pairs and the kicker
        >>> is_two_pair(['5C', '5S', '3C', '3S', '7H'])
        TwoPairResult(('5C', '5S'), ('3C', '3S'), '7H')

        >>> is_two_pair(['5C', '5S', '3C', '4S', '7H'])

        Note that the above call has None as result
    """
    first_pair, hand = find_pair(hand)
    if not first_pair:
        return None

    second_pair, hand = find_pair(hand)
    if not second_pair:
        return None

    return TwoPairResult(first_pair, second_pair, hand[0])

def is_one_pair(hand):
    """
        >>> is_one_pair(['5C', '5S', '4C', '3S', '7H'])
        OnePairResult(('5C', '5S'), ['7H', '4C', '3S'])

        x>>> is_two_pair(['5C', '5S', '3C', '4S', '7H'])

        Note that the above call has None as result
    """
    first_pair, hand = find_pair(hand)
    if not first_pair:
        return None

    second_pair, hand = find_pair(hand)
    if second_pair:
        raise NotImplementedError('is_one_pair got twopair')
        return None

    return OnePairResult(first_pair, hand)

class ThreeOfKindResult(ResultBase):
    def __init__(self, pair, kickers):
        ResultBase.__init__(self, ResultBase.THREE_OF_A_KIND)
        self.pair = pair
        self.kickers = sorted(kickers, cmp_cards_color)
        self.kickers.reverse()

    def __repr__(self):
        """
            >>> ThreeOfKindResult(('5C', '5S', '5H'), ['3S', '7H'])
            ThreeOfKindResult(('5C', '5S', '5H'), ['7H', '3S'])
        """
        return "ThreeOfKindResult(%s, %s)" % (self.pair, self.kickers)


    def __cmp_rank__(self, other):
        """
            >>> first = ThreeOfKindResult(('5C', '5S', '5H'), ['3S', '7H'])
            >>> first > ThreeOfKindResult(('5C', '5S', '5H'), ['3S', '6H'])
            True
            >>> first > ThreeOfKindResult(('4C', '4S', '4H'), ['3S', '7H'])
            True
        """
        if self.pair[0][0] > other.pair[0][0]:
            return 1
        elif self.pair[0][0] < other.pair[0][0]:
            return -1
        else:
            for pair in zip(self.kickers, other.kickers):
                r = cmp_cards(pair[0], pair[1])
                if r == 0:
                    continue
                return r

            return 0

        raise Exception("not implemented")


def find_three(hand):
    """ Find the next pair in the hand

        >>> find_three(['5C', '5S', '3S', '5H', '7H'])
        (('5C', '5S', '5H'), ['3S', '7H'])
    """
    hand = copy.copy(hand)
    for a in range(len(hand)):
        for b in range(a + 1, len(hand)):
            if hand[a][0] == hand[b][0]:
                for c in range(b + 1, len(hand)):
                    if hand[a][0] == hand[c][0]:
                        first_card = hand[a]
                        second_card = hand[b]
                        third_card = hand[c]
                        hand.remove(first_card)
                        hand.remove(second_card)
                        hand.remove(third_card)
                        return ((first_card, second_card, third_card), hand)

    return (None, hand)

def is_three_of_a_kind(hand):
    """
        >>> is_three_of_a_kind(['5C', '5S', '3S', '5H', '7H'])
        ThreeOfKindResult(('5C', '5S', '5H'), ['7H', '3S'])

        >>> is_three_of_a_kind(['5C', '5S', '3C', '4S', '7H'])

        Note that the above call has None as result
    """
    three_cards, hand = find_three(hand)
    if not three_cards:
        return None

    return ThreeOfKindResult(three_cards, hand)


def is_straight(hand):
    """
        x>>>is_straight(['KH', 'QS', '9D', 'TC', 'JS'])
        StraightResult(['KH', 'QS', 'JS', 'TC', '9D'])
    """


def parse_hands(line):
    """ parse one line from poker.txt
        >>> parse_hands('6S 8D KS 2D TH TD 9H JD TS 3S')
        (['6S', '8D', 'KS', '2D', 'TH'], ['TD', '9H', 'JD', 'TS', '3S'])
    """
    all_cards = line.strip().split(' ')
    return (all_cards[:5], all_cards[5:])

def get_result(cards):
    """
        get the highest ranking result

        >>> get_result(['5C', '5S', '3C', '3S', '7H'])
        TwoPairResult(('5C', '5S'), ('3C', '3S'), '7H')
    """
    retval = is_three_of_a_kind(cards)
    if retval:
        return retval

    retval = is_two_pair(cards)
    if retval:
        return retval

    retval = is_one_pair(cards)
    if retval:
        return retval

    raise NotImplementedError()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import sys
    if '-r' in sys.argv:
        print "Start"
        f = open('poker.txt')
        while True:
            line = f.readline()
            if line == "":
                break

            hands = parse_hands(line)
            try:
                result_one = get_result(hands[0])
                result_two = get_result(hands[1])

                if result_one == result_two:
                    print "!!! %s = %s" % (result_one, result_two)

                if  result_one.rank == ResultBase.THREE_OF_A_KIND or\
                    result_two.rank == ResultBase.THREE_OF_A_KIND:

                    if result_one > result_two:
                        print "%s > %s" % (result_one, result_two)
                    elif result_one < result_two:
                        print "%s < %s" % (result_one, result_two)
                    else:
                        print "%s = %s" % (result_one, result_two)

            except NotImplementedError:
                #~ print "%s   %s" % hands
                pass


        f.close()
