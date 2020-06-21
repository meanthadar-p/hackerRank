import pytest
from TheTimeInWords import the_time_in_words


@pytest.mark.parametrize("h, m, expected",
                         [
                             (5, 0, "five o' clock"),
                             (5, 1, "one minute past five"),
                             (5, 10, "ten minutes past five"),
                             (5, 15, "quarter past five"),
                             (5, 28, "twenty eight minutes past five"),
                             (5, 30, "half past five"),
                             (5, 40, "twenty minutes to six"),
                             (5, 45, "quarter to six"),
                             (5, 47, "thirteen minutes to six")
                         ])
def test_the_time_in_world(h, m, expected):
    result = the_time_in_words(h, m)
    assert result == expected
