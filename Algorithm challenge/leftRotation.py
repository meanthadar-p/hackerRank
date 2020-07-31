def left_rotation(arr, d):
    d = d % len(arr)

    if d != 0:
        arr = arr[d:len(arr)] + arr[0:d]

    return answer_format(arr)


def answer_format(arr):
    result = arr[0]
    for a in arr[1:len(arr)]:
        result = "{0} {1}".format(result, a)

    return result


arr = [1, 2, 3, 4, 5]
d = 0
print(left_rotation(arr, d))
