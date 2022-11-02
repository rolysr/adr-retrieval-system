from collections import deque


class Stack:
    """
        A stack data structure class for this project purposes.
        FIFO behavior
    """

    def __init__(self):
        self.__list = deque()

    def push(self, key):
        """
        Push an element at the top of the stack
        Arguments:
            key {object} -- element to push
        """
        self.__list.append(key)

    def pop(self):
        """
        Pop an element from the top of the stack
        Returns:
            element {object} -- element popped
        """
        return self.__list.pop()

    def peek(self):
        """
        Peek the element at the top of the stack
        Returns:
            element {object} -- element peek
        """
        key = self.__list.pop()
        self.__list.append(key)
        return key

    def is_empty(self):
        """
        Is stack empty?
        Returns:
            bool -- is or not empty
        """
        return len(self.__list) == 0

    def __str__(self):
        return "[" + ", ".join(self.__list) + "]"

    def __len__(self):
        return len(self.__list)