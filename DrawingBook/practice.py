import math


def drawing_book(number_of_pages, page):
    return min(start_turning_from_first(page), start_turning_from_last(number_of_pages, page))


def start_turning_from_first(page):
    return math.floor(page/2.)


def start_turning_from_last(number_of_pages, page):
    number_of_pages -= number_of_pages % 2
    diff = number_of_pages - page
    return math.ceil(diff/2.)
