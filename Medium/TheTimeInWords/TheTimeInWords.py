#
# Rank: MEDIUM
# Score: 25/25
# HackerRank Link: https://www.hackerrank.com/challenges/the-time-in-words/problem
#

# (5, 00, "five o' clock"), /
# (5, 01, "one minute past five"),
# (5, 10, "ten minutes past five"),
# (5, 15, "quarter past five"),
# (5, 28, "twenty eight minutes past five"),
# (5, 30, "half past five"),
# (5, 40, "twenty minutes to six"),
# (5, 45, "quarter to six"),
# (5, 47, "thirteen minutes to six")


import math


def the_time_in_words(h, m):
    if m == 0:
        return '{:s}{:s}'.format(number_mapping(h), time_mapping(0))

    if m <= 30:  # past
        conj = 1
        hour = h
    else:  # to
        conj = 2
        hour = (h+1) % 12
        m = 60 - m

    minute = number_mapping(m)
    if not minute:
        tens = tens_mapping(int(math.floor(m / 10)))
        units = number_mapping(m % 10)

        if not tens:
            minute = units + 'teen'
        elif not units:
            minute = tens
        else:
            minute = '{:s} {:s}'.format(tens, units)

    minute = minute_mapping(minute, m)

    return '{:s}{:s}{:s}'.format(minute,
                                 time_mapping(conj),
                                 number_mapping(hour))


def tens_mapping(t):
    return{
        2: 'twenty'
    }.get(t, None)


def number_mapping(n):
    return{
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        15: 'quarter',
        30: 'half'
    }.get(n, '')


def time_mapping(t):
    return{
        0: ' o\' clock',
        1: ' past ',
        2: ' to '
    }.get(t, '')


def minute_mapping(minute, m):
    if m == 15 or m == 30:
        return minute
    return{
        True: '{:s} minutes'.format(minute),
        False: '{:s} minute'.format(minute)
    }.get(m > 1, None)
