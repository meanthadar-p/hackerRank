def twoRobots(m, queries):
    total_distance = 0
    i_robot = [0, 0]

    for query in queries:
        d, i_robot = run_query(query, i_robot)
        total_distance += d

    return total_distance


def run_query(query, i_robot):
    d = 0
    n, is_first_step = select_robot(i_robot, query[0])

    if not is_first_step:
        d += abs(query[0] - i_robot[n])

    i_robot[n] = query[0]
    d += abs(query[1] - i_robot[n])
    i_robot[n] = query[1]

    print(d, i_robot)
    return d, i_robot


def select_robot(i_robot, container):
    if i_robot[0] == 0:
        return 0, True
    elif i_robot[1] == 0:
        return 1, True

    if abs(container - i_robot[0]) < abs(container - i_robot[1]):
        return 0, False
    else:
        return 1, False


m = 5
queries = [[1, 5], [3, 2], [4, 1], [2, 4]]
minimum = twoRobots(m, queries)
print(minimum)

m = 4
queries = [[1, 2], [4, 3]]
minimum = twoRobots(m, queries)
print(minimum)

m = 10
queries = [[2, 4], [5, 4], [9, 8]]
minimum = twoRobots(m, queries)
print(minimum)