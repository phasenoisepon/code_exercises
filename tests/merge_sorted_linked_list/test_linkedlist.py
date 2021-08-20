from unittest import TestCase
from merge_sorted_linked_list import SingleLinkedList
from merge_sorted_linked_list import Node
from merge_sorted_linked_list import merge_sorted


class TestSingleLinkedList(TestCase):
    def test_create_from_list_single(self):
        init_val = 1
        init_list = [init_val]
        my_sll = SingleLinkedList()
        my_sll.create_from_list(init_list)
        self.assertEqual(init_val, my_sll.head.data)

    def test_comprehensive(self):
        list1 = list(range(1, 10, 2))
        list2 = list(range(2, 10, 2))
        list3 = list1 + list2
        list3.sort()
        list4 = list(range(1, 10, 1))
        self.assertEqual(list3, list4)

        sll1 = SingleLinkedList()
        sll1.create_from_list(list1)
        sll2 = SingleLinkedList()
        sll2.create_from_list(list2)

        merged_sll = merge_sorted(sll1, sll2)
        merged_list = merged_sll.create_list()
        assert merged_list == list4


class TestNode(TestCase):
    def create_object(self):
        init_val = 5
        my_node = Node(init_val)
        self.assertEqual(my_node.data, init_val)
