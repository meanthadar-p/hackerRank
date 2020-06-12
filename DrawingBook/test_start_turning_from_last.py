from practice import start_turning_from_last
import pytest


@pytest.mark.parametrize("data, expected",
                         [
                             ([10, 5], 3),
                             ([10, 6], 2),
                             ([11, 5], 3),
                             ([11, 6], 2)
                         ])
def test_start_turning_from_last(data, expected):
    result = start_turning_from_last(data[0], data[1])
    assert result == expected
