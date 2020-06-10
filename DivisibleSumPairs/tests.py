from practice import divisible_sum_pairs
import pytest


@pytest.mark.parametrize("data, expected", [((6, 3, [1, 3, 2, 6, 1, 2]), 5)])
def test_normal_case(data, expected):
    result = divisible_sum_pairs(data[0], data[1], data[2])
    assert result == expected
