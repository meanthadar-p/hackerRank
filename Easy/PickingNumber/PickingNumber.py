#
# Rank: EASY
# Score: 20/20
# HackerRank Link: https://www.hackerrank.com/challenges/picking-numbers/problem?h_r=internal-search
#


def picking_number(arr):
    max_member_amount = 0
    for focus_idx in range(len(arr)):
        lower_member_amount = 0
        higher_member_amount = 0

        for sub_idx in range(focus_idx, len(arr)):
            if abs(arr[focus_idx] - arr[sub_idx]) <= 1:
                if arr[focus_idx] >= arr[sub_idx]:
                    lower_member_amount += 1
                if arr[focus_idx] <= arr[sub_idx]:
                    higher_member_amount += 1

        max_member_amount = max(max_member_amount, lower_member_amount, higher_member_amount)

    return max_member_amount
