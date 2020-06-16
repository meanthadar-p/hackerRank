import pytest
from PickingNumber import picking_number


@pytest.mark.parametrize("data, expected",
                         [
                             ([1, 2, 3, 2, 2, 1], 5),
                             ([1, 2, 1, 4, 5, 5], 3),
                             ([4, 2, 3, 4, 4, 9, 9, 8, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4], 22)
                         ])
def test_picking_number(data, expected):
    result = picking_number(data)
    assert result == expected
