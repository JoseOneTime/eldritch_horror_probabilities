# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\vrh\.spyder2\.temp.py
"""
from scipy.misc import comb

NORMAL = 2.0 / 6
BLESSED = 3.0 / 6
CURSED = 1.0 / 6
LUCKS = [NORMAL, BLESSED, CURSED]

def prob_exactly_n_hits(dice, n=1, luck=NORMAL):
    combs = comb([dice], [n])[0]
    prob_n_hits = luck ** n
    prob_dice_minus_n_misses = (1 - luck) ** (dice - n)
    return combs * prob_n_hits * prob_dice_minus_n_misses
    
def prob_n_or_more_hits(dice, n=1, luck=NORMAL):
    hitlist = range(n, dice+1)
    probs = [prob_exactly_n_hits(dice, h, luck) for h in hitlist]
    return ('%3s' % int(sum(probs) * 100)) + '%'
    
def print_prob_table(luck, luck_str):
    print luck_str
    DICE = range(1, 16)
    HITS = range(1, 5)
    X_LABEL = '  ' + ' '.join([('%4s' % d) for d in DICE])
    print X_LABEL
    for h in HITS:
        print h,
        print ' '.join([prob_n_or_more_hits(d, h, luck) for d in DICE])
    print ''
        
if __name__ == '__main__':
    print_prob_table(NORMAL, 'NORMAL')
    print_prob_table(BLESSED, 'BLESSED')
    print_prob_table(CURSED, 'CURSED')
    
            