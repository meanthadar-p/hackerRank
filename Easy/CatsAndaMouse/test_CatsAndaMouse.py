import pytest
from CatsAndaMouse import cats_and_a_mouse


@pytest.mark.parametrize("data, expected",
                         [
                             ((1, 4, 2), "Cat A"),
                             ((1, 2, 3), "Cat B"),
                             ((1, 3, 2), "Mouse C")
                         ])
def test_cats_and_a_mouse(data, expected):
    result = cats_and_a_mouse(data[0], data[1], data[2])
    assert result == expected
