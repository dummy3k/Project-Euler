#~ Peter has nine four-sided (pyramidal) dice, each with faces
#~ numbered 1, 2, 3, 4.
#~ Colin has six six-sided (cubic) dice, each with faces
#~ numbered 1, 2, 3, 4, 5, 6.
#~
#~ Peter and Colin roll their dice and compare totals: the highest total
#~ wins. The result is a draw if the totals are equal.
#~
#~ What is the probability that Pyramidal Pete beats Cubic Colin? Give your
#~ answer rounded to seven decimal places in the form 0.abcdefg

import sys
import random
import datetime
from pprint import pprint
from copy import copy

from euler_tools.misc import LossyPrinter

class NoMoreDices(Exception):
    pass

def inc_dices(dices, pos, max):
    """
        >>> inc_dices([1, 2, 3], 0, 6)
        [2, 2, 3]
        >>> inc_dices([6, 2, 3], 0, 6)
        [1, 3, 3]
        >>> inc_dices([6, 6, 3], 0, 6)
        [1, 1, 4]
        >>> inc_dices([6, 6, 6], 0, 6)
        Traceback (most recent call last):
            raise NoMoreDices()
        NoMoreDices
    """
    if dices[pos] + 1 <= max:
        dices[pos] += 1
        return dices
    elif pos + 1 >= len(dices):
        raise NoMoreDices()
    else:
        dices[pos] = 1
        return inc_dices(dices, pos + 1, max)


def solve(faces, cnt_dices):
    results = [0 for n in range(faces * cnt_dices)]
    colins_dices = [1 for n in range(cnt_dices)]
    try:
        while True:
            colins_score = reduce(lambda x,y: x + y, colins_dices)
            results[colins_score - 1] += 1

            colins_dices = inc_dices(colins_dices, 0, faces)
    except NoMoreDices:
        pass

    return results

def solve6():
    lp = LossyPrinter(1)
    peters_dices = [1 for n in range(9)]
    peter_win = 0
    cnt_games = 0
    try:
        while True:
            lp.try_print("%s" % peters_dices)
            peters_dices = inc_dices(peters_dices, 0, 4)
            peters_score = reduce(lambda x,y: x + y, peters_dices)

            colins_dices = [1 for n in range(6)]
            try:
                while True:
                    colins_dices = inc_dices(colins_dices, 0, 6)
                    colins_score = reduce(lambda x,y: x + y, colins_dices)
                    cnt_games += 1
                    if peters_score > colins_score:
                        peter_win += 1
            except NoMoreDices:
                pass

    except NoMoreDices:
        pass

    print "cnt_games: %s" % cnt_games
    print "peter_win: %s" % peter_win
    print("%.7f" % (peter_win / float(cnt_games)))

def solve3():
    peter_win = 0
    for peter in range(1, 5):
        for colin in range(1, 7):
            if peter > colin:
                peter_win += 1

    answer = peter_win / 24.
    print "%.7f" % answer


sysrnd = random.SystemRandom()

def throw_dices(heads, count):
    dices = [sysrnd.randrange(1, heads + 1) for n in range(count)]

    #~ good = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    #~ dices.sort()
    #~ if not dices in good:
        #~ raise Exception("bad: %s" % dices)

    #~ print dices
    return reduce(lambda x,y: x + y, dices, 0)

    #~ sum = 0
    #~ for n in range(count):
        #~ sum += random.randrange(1, heads + 1)
#~
    #~ return sum

def solve2(peter_head_cnt, peter_dice_cnt, colin_head_cnt, colin_dice_cnt):
    lp = LossyPrinter(1)

    peter_win = 0
    cnt_games = 0
    ende = datetime.datetime.now() + datetime.timedelta(seconds=30)
    while datetime.datetime.now() < ende:
    #~ for n in range(100000):
        cnt_games += 1
        peter = throw_dices(peter_head_cnt, peter_dice_cnt)
        colin = throw_dices(colin_head_cnt, colin_dice_cnt)
        #~ print "%s, %s" % (peter,
        if peter > colin:
            peter_win += 1

        # 0.4120098
        lp.try_print("%.7f" % (peter_win / float(cnt_games)))

    return peter_win / float(cnt_games)
    #~ print peter_win


def combine(token, values):
    """
        >>> combine(1, [2, 3])
        [1, 2, 3]
    """
    retval = [token]
    retval.extend(values)
    return retval

def permutate(tokens, width):
    """
        permutate input, ignoring token position

        >>> permutate([1, 2, 3], 1)
        [[1], [2], [3]]

        >>> permutate([1, 2, 3], 2)
        [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    """
    #~ print "permutate(%s, %s)" % (tokens, width)

    if width < 0:
        raise Exception("invalid value")

    if width == 1:
        return [[item] for item in tokens]

    result = []
    sub_tokens = permutate(tokens, width - 1)
    for token in tokens:
        for sub_token in sub_tokens:
            bar = combine(token, sub_token)
            result.append(bar)
    return result


def permutate_unique(tokens, width, dbg=False):
    """
        permutate input, ignoring token position

        >>> permutate_unique([1, 2, 3], 1)
        [[1], [2], [3]]

        >>> permutate_unique([2, 3], 1)
        [[2], [3]]

        >>> permutate_unique([1, 2, 3], 2)
        [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]

        >>> permutate_unique([1, 2], 2)
        [[1, 1], [1, 2], [2, 2]]

        >>> permutate_unique([1, 2], 3)
        [[1, 1, 1], [1, 1, 2], [1, 2, 2], [2, 2, 2]]

    """
    if dbg:
        print "permutate_unique(%s, %s)" % (tokens, width)

    if width < 0:
        raise Exception("invalid value")

    if width == 1:
        return [[item] for item in tokens]

    result = []
    for index, token in enumerate(tokens):
        results = permutate_unique(tokens[index:], width - 1)
        results = map(lambda x: combine(token, x), results)
        #~ for result in results:
        #~ bar = combine(token, results)
        result.extend(results)

    return result

    #~ for sub_token in permutate(tokens, width - 1):
        #~ bar = combine(tokens[0], sub_token)
        #~ result.append(bar)
#~
    #~ for item in tokens[1:]:
        #~ bar = [item for n in range(width)]
        #~ result.append(bar)

    #~ for index, token in enumerate(tokens):
        #~ bar = combine(token, sub_tokens)
        #~ result.append(bar)


def pprint_array(a, rows = 3):
    if len(a) < rows * 2:
        pprint(a)
        return

    pprint(a[:rows])
    print("...")
    pprint(a[-rows:])

def solve4(peter_head_cnt, peter_dice_cnt, colin_head_cnt, colin_dice_cnt):
    answer = 0
    #~ peters_dices_all = permutate_unique(range(1, peter_head_cnt + 1), peter_dice_cnt)
    #~ colins_dices_all = permutate_unique(range(1, colin_head_cnt + 1), colin_dice_cnt)
    peters_dices_all = permutate(range(1, peter_head_cnt + 1), peter_dice_cnt)
    colins_dices_all = permutate(range(1, colin_head_cnt + 1), colin_dice_cnt)

    pprint_array(peters_dices_all, 8)
    pprint_array(colins_dices_all, 8)

    for peters_dices in peters_dices_all:
        for colins_dices in colins_dices_all:
            peters_score = reduce(lambda x,y: x + y, peters_dices, 0)
            colins_score = reduce(lambda x,y: x + y, colins_dices, 0)
            if peters_score > colins_score:
                #~ print "WIN %s vs. %s" % (peters_dices, colins_dices)
                answer += 1

    print "wins: %.7f" % answer
    answer = answer / float(len(peters_dices_all) * len(colins_dices_all))
    #~ print "0.abcdefg"
    print "%.7f" % answer
    guess = 0.573
    if abs(answer - guess) > 0.001:
        print "INCORRECT (should be ~%s)" % guess

    return answer


def solve5():
    peters_results = solve(4, 9)
    colins_results = solve(6, 6)

    sum_peter = reduce(lambda x,y: x + y, peters_results)
    sum_colin = reduce(lambda x,y: x + y, colins_results)

    print "Score\tPeter\tColin\tC'Loses\tP'hit\tC'Lost"
    colin_loses = 0
    answer = 0
    for score, (p, c) in enumerate(zip(peters_results, colins_results)):
        p_hit = float(p) / sum_peter
        bar = float(colin_loses) / sum_colin
        print "%s\t%s\t%s\t%s\t%.2g\t%.2g\t%s" % (score, p, c, colin_loses, p_hit, bar, c * colin_loses)

        answer += c * colin_loses

        colin_loses += c

    print "Sum:\t%s\t%s\t\t\t\t%s" % (sum_peter, sum_colin, answer)

    print float(answer) / (sum_peter * sum_colin)

    #    1015970930
    #   12230590464
    #~ print "%s, %s" % (len(peters_results), len(colins_results))
    #~ pprint(zip(peters_results, colins_results))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #~ solve4(2, 1, 2, 1)
    peter_head_cnt = 4
    peter_dice_cnt = 9
    colin_head_cnt = 6
    colin_dice_cnt = 6

    if '-2' in sys.argv:
        guess = solve2(peter_head_cnt, peter_dice_cnt, colin_head_cnt, colin_dice_cnt)
    else:
        guess = None

    if '-4' in sys.argv:
        answer = solve4(peter_head_cnt, peter_dice_cnt, colin_head_cnt, colin_dice_cnt)
        if guess:
            delta = abs(answer - guess)
            print "delta: %s" % delta


    if '-5' in sys.argv:
        solve5()
