from tests1 import SortAlgorithms
import pytest
import random

@pytest.fixture
def algorithms():
    return SortAlgorithms()


@pytest.fixture
def random_list():
    return random.sample(range(100), 5)

@pytest.mark.parametrize(
    'random_list',
    [
        [-2, 10, 2],
        [2, 5, 1, 9],
        [10, 21, 13, 3, -19]
    ]
)
def test_result(algorithms, random_list):
    assert algorithms.bubble_sort(random_list.copy()) == sorted(random_list.copy())


# def test_typeerror(algorithms, random_list):
#     with pytest.raises(TypeError):
#         algorithms.bubble_sort(tuple(random_list))
#
#
# def test_valueerror(algorithms):
#     with pytest.raises(TypeError):
#         algorithms.bubble_sort(1, 'a', 22, 2)
