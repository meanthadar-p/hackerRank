#
# Rank: EASY
# Score: 15/15
# HackerRank Link: https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen
#


def electronics_shop(keyboards, drives, budget):
    max_price = -1
    for keyboard in keyboards:
        for drive in drives:
            if max_price < drive + keyboard <= budget:
                max_price = drive + keyboard
    return max_price
