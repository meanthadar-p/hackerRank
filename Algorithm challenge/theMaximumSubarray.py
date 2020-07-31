def maxSubarray(arr):
    return find_max_subarray(arr), find_max_subsequence(arr)


def find_max_subarray(arr):
    if max(arr) < 0:
        return max(arr)

    subarrays = find_subarrays(arr)
    return 0


def find_subarrays(arr):
    results = list()

    return results


def find_max_subsequence(arr):
    if max(arr) < 0:
        return max(arr)

    subsequence = 0

    for a in arr:
        if a > 0:
            subsequence += a
    return subsequence


arr = [-1, -2, -3, -4]
print(maxSubarray(arr))
