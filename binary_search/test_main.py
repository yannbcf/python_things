from main import binary_search

import unittest
import warnings
import timeit

class BinarySearchTest(unittest.TestCase):
    def test_non_sorted_list(self):
        list = [0, 2, 3, 1, 4]
        with self.assertWarns(UserWarning):
            binary_search(list, 1, True)

        list = [0, 2, 3, 1, 4]
        with warnings.catch_warnings(record=True) as warning_list:
            binary_search(list, 1)
            self.assertEqual(len(warning_list), 0)

    def test_search(self):
        list = [0, 1, 2, 3, 4, 5, 6]

        index_0 = binary_search(list, 0)
        self.assertEqual(index_0, 0)
        self.assertEqual(list[index_0], 0)

        index_2 = binary_search(list, 2)
        self.assertEqual(index_2, 2)
        self.assertEqual(list[index_2], 2)

        index_4 = binary_search(list, 4)
        self.assertEqual(index_4, 4)
        self.assertEqual(list[index_4], 4)

        index_6 = binary_search(list, 6)
        self.assertEqual(index_6, 6)
        self.assertEqual(list[index_6], 6)

    def _test_performances_factor(self, factor: int, target: int):
        l = list(range(factor))

        time_execution_1 = timeit.timeit(lambda: list.index(l, target), number=1000)
        average_time_1 = (time_execution_1 / 1000) * 1000

        time_execution_2 = timeit.timeit(lambda: binary_search(l, target), number=1000)
        average_time_2 = (time_execution_2 / 1000) * 1000

        self.assertLess(average_time_2, average_time_1)
        print(f"The binary search is faster by: {average_time_1 - average_time_2} ms (factor {factor})")

    def test_performances(self):
        self._test_performances_factor(1_000, 500)
        self._test_performances_factor(100_000, 50_000)
        self._test_performances_factor(100_000_000, 500_000) ## not too large otherwise list.index takes too much time

if __name__ == "__main__":
    unittest.main()
