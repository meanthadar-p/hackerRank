import unittest
from practice import divisible_sum_pairs


class DivisibleSumPairsTests(unittest.TestCase):
    def test_normal_case(self):
        result = divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2])
        act = 5
        self.assertEqual(result, act, 'result should be %d but actually got %d' % (act, result))
        

if __name__ == '__main__':
    unittest.main()
