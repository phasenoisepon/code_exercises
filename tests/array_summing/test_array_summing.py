from unittest import TestCase
from array_summing import ArraySumming


class Test(TestCase):

    def test_sum_two_target(self):
        list1 = [5, 7, 1, 2, 8, 4, 3]
        search1 = 10
        self.assertTrue(ArraySumming.sum_two_target(list1, search1))

    def test_sum_two_target_self_reference(self):
        """
        Check for self comparison
        for example [5, 1, 2] checking for sum of 10, 5 could be compared to 5 *incorrectly*
        :return:
        """
        list1 = [5, 1, 2]
        search1 = 10
        self.assertFalse(ArraySumming.sum_two_target(list1, search1))

    def test_sum_two_target_repeated_number(self):
        """
        Check that a repeated number passes
        :return:
        """
        list1 = [5, 5, 1, 2]
        search1 = 10
        self.assertTrue(ArraySumming.sum_two_target(list1, search1))

    def test_sum_two_target_naive(self):
        list1 = [5, 7, 1, 2, 8, 4, 3]
        search1 = 10
        self.assertTrue(ArraySumming.sum_two_target_naive(list1, search1))

    def test_sum_two_target_naive_self_reference(self):
        """
        Check for self comparison
        for example [5, 1, 2] checking for sum of 10, 5 could be compared to 5 *incorrectly*
        :return:
        """
        list1 = [5, 1, 2]
        search1 = 10
        self.assertFalse(ArraySumming.sum_two_target_naive(list1, search1))

    def test_sum_two_target_naive_repeated_number(self):
        """
        Check that a repeated number passes
        :return:
        """
        list1 = [5, 5, 1, 2]
        search1 = 10
        self.assertTrue(ArraySumming.sum_two_target_naive(list1, search1))
