import pytest
from CountingValleys import counting_valleys


@pytest.mark.parametrize("data, expected",
                         [
                            ("UUDUUUDDDD", 0),
                            ("UDDDUDUU", 1)
                         ])
def test_counting_valleys(data, expected):
    result = counting_valleys(data)
    assert result == expected
