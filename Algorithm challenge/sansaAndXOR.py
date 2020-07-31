def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0

    result = 0
    for i in range(0, len(arr), 2):
        result ^= arr[i]

    return result


x = [3, 4, 5]
print(sansaXor(x))


# 1 number
# 1 = 1
#
# 2 number
# 1 = 2
# 2 = 2
#
# 3 number
# 1 = 3
# 2 = 4
# 3 = 3
#
# 4 number
# 1 = 4
# 2 = 6
# 3 = 6
# 4 = 4
#
# 5 number
# 1 = 5
# 2 = 8
# 3 = 9
# 4 = 8
# 5 = 5
#
# 6 number
# 1 = 6
# 2 = 10
# 3 = 12
# 4 = 12
# 5 = 10
# 6 = 6
#
# 7 number
# 1 = 7
# 2 = 12
# 3 = 15
# 4 = 16
# 5 = 15
# 6 = 12
# 7 = 7

# 1, n = n
# 2, n-1 = (n-1) * 2
# 3, n-2 = (n-2) * 3
# 4, n-3 = (n-3) * 4
# ...
# x, n - x + 1 = (n - x + 1) * x   ; x <= math.ceil(n/2.)   XXXXX didn't use lol XXXXXX

# if amount == even: ignore this number
# else pick up just 1 of odd index
