from main import find_largest_values

import unittest
import warnings

class HeapQueueTest(unittest.TestCase):
    def test_invalid_list(self):
        with self.assertWarns(UserWarning):
            result = find_largest_values([], 3)
            self.assertEqual(result, [])

        with self.assertWarns(UserWarning):
            result = find_largest_values(["w"], 2)
            self.assertEqual(result, [])

    def test_find_largest_numbers(self):
        list = [11, 7, 8, 3, 1, 2, 3]
        with warnings.catch_warnings(record=True) as warning_list:
            result = find_largest_values(list, 3)
            self.assertEqual(len(warning_list), 0)
            self.assertEqual(result, [11, 8, 7])

    def test_find_highest_chars(self):
        list = ["a", "b", "z", "w", "x"]
        with warnings.catch_warnings(record=True) as warning_list:
            result = find_largest_values(list, 3)
            self.assertEqual(len(warning_list), 0)
            self.assertEqual(result, ["z", "x", "w"])

if __name__ == "__main__":
    unittest.main()
