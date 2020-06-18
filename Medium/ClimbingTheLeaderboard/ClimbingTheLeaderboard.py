#
# Rank: MEDIUM
# Score: 20/20
# HackerRank Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#


# BigO(m+n log(m)):
def climbing_the_leader_board(scores, alice):
    a_rank = []
    leader_board = create_leader_board(scores)  # BigO(m)

    for score in alice:  # BigO(n)
        rank = finding_ranking(leader_board, score, 0, len(leader_board)-1)  # BigO(log m)
        a_rank.append(rank)

    return a_rank


def create_leader_board(scores):  # BigO(m)
    leader_board = []
    for idx in range(len(scores)):
        if len(leader_board) == 0:
            leader_board.append(scores[idx])
        elif scores[idx] != leader_board[-1]:
            leader_board.append(scores[idx])

    return leader_board


def finding_ranking(leader_board, score, f, l):  # BigO(log m)
    if f == l:
        if score >= leader_board[f]:
            return f+1
        elif score < leader_board[f]:
            return f+2

    middle = int((f+l)/2)

    if score == leader_board[middle]:
        return middle+1
    elif score > leader_board[middle]:
        l = max(f, middle - 1)
    else:
        f = min(middle + 1, l)

    return finding_ranking(leader_board, score, f, l)

# BigO(mn) over times
# def climbing_the_leader_board(scores, alice):
#     ranking = []
#     for a_score in alice:
#         rank = 0
#         for idx in range(len(scores)):
#             if a_score >= scores[idx]:
#                 ranking.append(rank+1)
#                 break
#             elif idx == len(scores)-1:
#                 ranking.append(rank+2)
#                 break
#
#             if not isSameScoreAsPrevious(scores, idx):
#                 rank += 1
#
#     return ranking
#
#
# def isSameScoreAsPrevious(scores, index):
#     if index-1 < 0:
#         return False
#
#     return scores[index] == scores[index-1]
