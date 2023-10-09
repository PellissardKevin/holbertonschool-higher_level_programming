#!/usr/bin/python3
"""Defines a 'Node' class for a linked list"""


class Node:
    """Definition of a node"""
    def __init__(self, data, next_node=None):
        """Inits Node with data and next_node."""
        if not type(data) is int:
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or type(next_node) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(data) is int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Inits SinglyLinkedList with a head."""
        self.__head = None

    def __str__(self):
        tmp = self.__head
        datas = []
        while (tmp is not None):
            datas.append("{:d}".format(tmp.data))
            tmp = tmp.next_node
        return "\n".join(datas)

    def sorted_insert(self, value):
        tmp = self.__head
        new = Node(value)
        if tmp is None:
            self.__head = new
            return
        if value < tmp.data:
            new.next_node = tmp
            self.__head = new
            return
        while (tmp.next_node is not None and value > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
