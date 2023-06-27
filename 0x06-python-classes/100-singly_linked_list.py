#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns value of data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node.

        Args:
            value (int): The data value to set.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value (Node): The next node to set.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize a SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list

        Args:
            value (int): The data value of the new node to insert.
        """
        n_node = Node(value)
        if self.head is None:
            self.head = n_node
        elif value < self.head.data:
            n_node.next_node = self.head
            self.head = n_node
        else:
            curr = self.head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            n_node.next_node = curr.next_node
            curr.next_node = n_node

    def __str__(self):
        """Return a string representation of the linked list."""
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(nodes)
