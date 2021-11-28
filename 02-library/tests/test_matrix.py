from cs506.matrix import get_determinant
import pytest


@pytest.mark.parametrize('test_input,expected_data', [
    ([[7, 6, 1, -4], [5, 2, -1, 3], [-1, 4, 9, 2], [3, 8, 5, 6]], -1792),
    ([[-3.2, 1.3, 5.4], [7.8, 9.6, 12.5], [0.9, 8.3, 3.6]], 502),
])
def test_matrix(test_input, expected_data):
    print(test_input)
    actual_data = get_determinant(test_input)
    assert int(actual_data) == expected_data
