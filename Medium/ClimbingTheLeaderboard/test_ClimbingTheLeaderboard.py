import pytest
from ClimbingTheLeaderboard import climbing_the_leader_board


@pytest.mark.parametrize("data, expected",
                         [
                             (([100, 90, 90, 80, 75, 60], [50, 65, 77, 85, 90, 102]), [6, 5, 4, 3, 2, 1]),
                             (([100, 90, 90, 80, 75], [50, 77, 85, 90, 99, 105]), [5, 4, 3, 2, 2, 1])
                         ])
def test_climbing_the_leader_board(data, expected):
    result = climbing_the_leader_board(data[0], data[1])
    assert result == expected
