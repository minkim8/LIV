import unittest
from Solution import graph
from Solution import MAX_LENGTH

# Creating unittest
class TestDifferentGraphs(unittest.TestCase):

    def test_no_path_zero_check(self):
        # Testing a=b returns 0
        result = graph[1][1]
        self.assertEqual(result,0)

    def test_no_path_zero_check2(self):
        # Testing a=b returns 0 2nd
        result = graph[3][3]
        self.assertEqual(result,0)

    def test_check_max_length(self):
        # Checking the maximum length of the graph
        self.assertEqual(MAX_LENGTH,4)

    def test_check_min_distance_example(self):
        # Testing one example of calculated minimum distance
        result = graph[0][2]
        self.assertEqual(result,12)

