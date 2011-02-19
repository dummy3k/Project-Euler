import unittest

def is_high_card(hand):
    return true

def find_pair(hand):
    pair = None
    for a in range(len(hand)):
        for b in range(a + 1, len(hand)):
            if hand[a][0] == hand[b][0]:
                #~ pair = (a, b)
                first_card = hand[a]
                second_card = hand[b]
                hand.remove(hand[a])
                hand.remove(hand[b])
                return (first_card, second_card, hand)

def is_two_pair(hand):

    if not pair:
        return False

    return True

#~ Club
#~ Spade
#~ Heard
#~ Diamonds

#class TestProblem(unittest.TestCase):
    #def testResult(self):
        #hand_one = ["8C", "TS", "KC", "9H", "4S"]
        ##~ hand_two = 7D 2S 5D 3S AC

        #self.assertTrue(is_two_pair(["5C", "5S", "3C", "3S", "7H"]))
        ##~ self.assertFalse(is_two_pair(["5C", "5S", "4C", "3S", "7H"]))
        #self.assertFalse(is_two_pair(["1C", "5S", "4C", "3S", "7H"]))

if __name__ == '__main__':
    unittest.main()
