"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    """
    singly linked list implementation
    """

    def __init__(self):
        self.head = None

    def create_from_list(self, input_list: list) -> None:
        assert self.head is None
        if len(input_list) < 1:
            return
        for item in input_list:
            self.insert_at_end(item)

    def insert_at_beginning(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            tmp.next = self.head
            self.head = tmp

    def insert_at_end(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = tmp


def merge_sorted(list1: SingleLinkedList, list2: SingleLinkedList) -> SingleLinkedList:

    return SingleLinkedList()


def main():
    pass


if __name__ == "__main__":
    main()
