from unittest import TestCase
from missing_number import MissingNumbers
from random import shuffle

class TestMissingNumbers(TestCase):
    def test_sum_1_n(self):
        self.assertEqual(MissingNumbers.sum_1_n(1), 1)
        self.assertEqual(MissingNumbers.sum_1_n(2), 3)
        self.assertEqual(MissingNumbers.sum_1_n(3), 6)

        n = 100
        # reminder that range is [start, stop)
        self.assertEqual(MissingNumbers.sum_1_n(n), sum(range(1, n + 1, 1)))
        # self.fail()

    def test_find_missing(self):
        test_list = [1, 2, 3, 4, 5]
        n = len(test_list) + 1  # 6 was 'removed' from the list
        self.assertEqual(6, MissingNumbers.find_missing(test_list, n))

        n = 500
        generated_list = list(range(1, n + 1, 1))
        shuffle(generated_list)
        removed_element = generated_list.pop()
        self.assertEqual(removed_element, MissingNumbers.find_missing(generated_list, n))

    def test_find_missing_set(self):
        test_list = [1, 2, 3, 4, 5]
        n = len(test_list) + 1  # 6 was 'removed' from the list
        self.assertEqual(6, MissingNumbers.find_missing_set(test_list, n))

        n = 500
        generated_list = list(range(1, n+1, 1))
        shuffle(generated_list)
        removed_element = generated_list.pop()
        self.assertEqual(removed_element, MissingNumbers.find_missing_set(generated_list, n))
