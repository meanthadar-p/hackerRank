# TODO: How to import QuickSort
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.realpath('..'))+'/lib')
# import QuickSort
import math


def sort_low_to_high(arr):
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
    return arr


def quick_sort(arr, left, right):
    if left < right:
        center = partition(arr, left, right)

        quick_sort(arr, left, center-1)
        quick_sort(arr, center+1, right)


def partition(arr, left, right):
    center = math.floor((left + right)/2)

    while left < right:
        while arr[left] < arr[center]:
            left += 1
        while arr[right] > arr[center]:
            right -= 1

        if left != right:
            arr[left], arr[right] = arr[right], arr[left]
            center = left if center == right else (right if center == left else center)
    return center
