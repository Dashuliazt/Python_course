import unittest
from tests1 import SortAlgorithms

class TESTBubbleSort(unittest.TestCase):

    def setUp(self):
        self.algorithms = SortAlgorithms()


    def tearDown(self):
        del self.algorithms


    def test_result(self):
        self.assertEqual(self.algorithms.bubble_sort([3, 2, 1, 10, 5]), [1, 2, 3, 5, 10])


    def test_typeerror(self):
        with self.assertRaises(TypeError):
            self.algorithms.bubble_sort((1, 3, 7, -1))

