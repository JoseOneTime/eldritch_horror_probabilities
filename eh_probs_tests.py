# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:45:31 2014

@author: vrh
"""
import unittest
from eh_probs import prob_exactly_n_hits, prob_n_or_more_hits

class TestEhProbs(unittest.TestCase):
    
    def test_probs_sum_to_one(self):
        """ Ensure that sum of all probabilities equals 1. """
        DICE = 3
        all_hits_nums = range(DICE+1)
        probs = [prob_exactly_n_hits(DICE, n) for n in all_hits_nums]
        self.assertAlmostEqual(sum(probs), 1, 2)
        
    def test_prob_greater_with_more_dice(self):
        d3 = prob_n_or_more_hits(3)
        d2 = prob_n_or_more_hits(2)
        self.assertGreaterEqual(d3, d2)