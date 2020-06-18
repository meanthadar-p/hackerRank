#
# Rank: EASY
# Score: 15/15
# HackerRank Link:
#   https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#


def cats_and_a_mouse(cat_a, cat_b, mouse_c):
    diff_cat_a = abs(mouse_c - cat_a)
    diff_cat_b = abs(mouse_c - cat_b)

    if diff_cat_a < diff_cat_b:
        return "Cat A"
    elif diff_cat_a > diff_cat_b:
        return "Cat B"
    else:
        return "Mouse C"
