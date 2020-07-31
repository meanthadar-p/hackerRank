def superDigit(n, k):
    result = recursive_sum_digit(n)
    return recursive_sum_digit(str(result * k))


def recursive_sum_digit(number):
    number = list(number)
    sum_digit = 0

    for digit in number:
        sum_digit += int(digit)

    if sum_digit > 10:
        sum_digit = recursive_sum_digit(str(sum_digit))

    return sum_digit


print(superDigit("123", 3))
