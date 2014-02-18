import eldritch_horror_probabilities as eh
import unittest

LUCK = eh.NORMAL
    
class Eh_Tests(unittest.TestCase):

    # test methods must start with 'test'

    def test_more_dice_increase_probability(self):
        two_dice = eh.prob_n_or_more_hits(2, 1, LUCK)
        three_dice = eh.prob_n_or_more_hits(3, 1, LUCK)
        self.assertLessEqual(two_dice, three_dice)

    def test_prob_n_or_more_greater_than_exactly_n(self):
        prob_n = eh.prob_exactly_n_hits(3, 1, LUCK)
        prob_n_or_more = eh.prob_n_or_more_hits(3, 1, LUCK)
        self.assertLessEqual(prob_n, prob_n_or_more)

    def test_no_negative_probs(self):
        for dice in eh.DICE_ROLLED:
            prob = eh.prob_n_or_more_hits(dice, 3, LUCK)
            self.assertGreaterEqual(prob, 0.0)

if __name__ == '__main__':
    unittest.main()
