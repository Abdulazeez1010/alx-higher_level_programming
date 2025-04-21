#!/usr/bin/python3
"""
This module defines two classes for creating ans managing a singly linked list:

- Node: Represents an element of the list.
- SinglyLinkedList: Manages the linked list allows sorted insertion.
"""


class Node:
    """This class defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes a New node with given data and optional next node

        Args:
            data(int): The value to store in the node.
            next_node (Node or None): The next node in the linked list,
            default to none.

        Raises:
            TypeError: If data is not an integer.
            TypeError: if next_node is not a Node object or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list (one data per line)"""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
