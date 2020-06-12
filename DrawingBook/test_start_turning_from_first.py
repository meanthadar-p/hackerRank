from DrawingBook import start_turning_from_first
import pytest


@pytest.mark.parametrize("data, expected",
                         [
                             (6, 3),
                             (7, 3),
                             (8, 4),
                             (9, 4)
                         ])
def test_start_turning_from_first(data, expected):
    result = start_turning_from_first(data)
    assert result == expected
