import pytest
from QuickSort import sort_low_to_high


@pytest.mark.parametrize("data, expected",
                         [
                            ([5, 3, 7, 6, 2, 4], [2, 3, 4, 5, 6, 7]),
                            ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),
                         ])
def test_quick_sort(data, expected):
    result = sort_low_to_high(data)
    assert result == expected
