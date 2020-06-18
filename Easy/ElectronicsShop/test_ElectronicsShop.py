import pytest
from ElectronicsShop import electronics_shop


@pytest.mark.parametrize("data, expected",
                         [
                             (([3, 1], [5, 2, 8], 10), 9),
                             (([4], [5], 5), -1),
                             (([40, 50, 60], [5, 8, 12], 58), 58)
                         ])
def test_electronics_shop(data, expected):
    result = electronics_shop(data[0], data[1], data[2])  # keyboards, drives, budget
    assert result == expected
