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
        if len(input_list) == 1:
            self.head = Node(input_list[0])
            return

        current = self.head
        for item in input_list:
            if self.head is None:
                self.head = Node(item)
            else:
                current.next = Node(item)
                current = current.next


def merge_sorted(list1: SingleLinkedList, list2: SingleLinkedList) -> SingleLinkedList:

    return SingleLinkedList()


def main():
    pass


if __name__ == "__main__":
    main()
