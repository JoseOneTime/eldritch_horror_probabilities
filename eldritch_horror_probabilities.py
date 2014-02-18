NORMAL = 1.0 / 3
BLESSED = 1.0 / 2
CURSED = 1.0 / 6
DICE_ROLLED = range(1, 16)
HITS_NEEDED = range(1, 5)

def prob_exactly_n_hits(dice, n, luck):
    return (luck ** n) * ((1-luck) ** (dice - n))

def prob_n_or_more_hits(dice, n, luck):
    if n > dice:
        prob_enough = 0.0
    else:
        prob_too_few = sum([prob_exactly_n_hits(dice, hits, luck) for hits in range(n)])
        prob_enough = 1 - prob_too_few
    return prob_enough

def success_probability(dice, hits_needed=1, luck=NORMAL):
    """ Probability that rolling 'dice' will result in 'hits_needed' or more """    
    prob = prob_n_or_more_hits(dice, hits_needed, luck)
    return `int(round(prob, 2) * 100)` + '%'

def print_prob_table(luck):
    print '    ' + '  '.join([('%4s' % d) for d in DICE_ROLLED])
    for h in HITS_NEEDED:
        row = [str(h)]
        for d in DICE_ROLLED:
            row.append('%4s' % success_probability(d, h, luck))
        print '  '.join(row)

if __name__ == '__main__':
    print 'Normal'
    print_prob_table(NORMAL)
    print '\nBlessed'
    print_prob_table(BLESSED)
    print '\nCursed'
    print_prob_table(CURSED)

