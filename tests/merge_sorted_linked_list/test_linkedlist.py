from unittest import TestCase
from merge_sorted_linked_list import SingleLinkedList
from merge_sorted_linked_list import Node

class TestSingleLinkedList(TestCase):
    def test_create_from_list_single(self):
        init_val = 1
        init_list = [init_val]
        my_SLL = SingleLinkedList()
        my_SLL.create_from_list(init_list)
        self.assertEqual(init_val, my_SLL.head.data)

class TestNode(TestCase):
    def create_object(self):
        init_val = 5
        my_node = Node(init_val)
        self.assertEqual(my_node.data, init_val)