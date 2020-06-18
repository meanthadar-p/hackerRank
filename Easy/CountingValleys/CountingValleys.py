#
# Rank: EASY
# Score: 15/15
# HackerRank Link: https://www.hackerrank.com/challenges/counting-valleys/problem
#


def counting_valleys(steps):
    print(steps)
    previous_level = 0
    level = 0
    mountains = 0
    valleys = 0
    for step in steps:
        level += mapping_step(step)
        print(step, level)

        if previous_level == 0:
            if level > 0:
                mountains += 1
            elif level < 0:
                valleys += 1

        previous_level = level

    print("mountains: ", mountains)
    print("valleys: ", valleys)
    return valleys


def mapping_step(x):
    return{
        'U': 1,
        'D': -1
    }.get(x, 0)
