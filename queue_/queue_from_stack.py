# pylint: disable=duplicate-code
"""
Programming for linguists

Implementation of the data structure "Queue" from stack
"""

from stack.stack import Stack
from queue_.queue_ import TooManyElementsInQueueError, TypeCapacityError, QueueIsFullError


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Stack = Stack(),  capacity: int = 0):
        if not isinstance(data, Stack):
            raise TypeError

        if not isinstance(capacity, int):
            raise TypeCapacityError

        self._q_capacity = capacity

        if data.size() > self._q_capacity and data.size() and self._q_capacity:
            raise TooManyElementsInQueueError
        self.data = data

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if self.full():
            raise QueueIsFullError

        return self.data.push(element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        if self.empty():
            raise IndexError

        tmp_stack = Stack()
        while self.data.data:
            tmp_stack.push(self.data.top())
            self.data.pop()
        top_item = tmp_stack.top()
        tmp_stack.pop()
        while tmp_stack.data:
            self.data.push(tmp_stack.top())
            tmp_stack.pop()

        return top_item

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return self.data.empty()

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return self.data.size()

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        if self.empty():
            raise IndexError

        tmp_stack = Stack()
        while self.data.data:
            tmp_stack.push(self.data.top())
            self.data.pop()
        top_item = tmp_stack.top()
        while tmp_stack.data:
            self.data.push(tmp_stack.top())
            tmp_stack.pop()

        return top_item

    def capacity(self):
        """
        Return the capacity of queue_
        :return: the number of elements which can be in queue_
        """
        return self._q_capacity

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        if not self._q_capacity:
            return False  # if capacity == 0, the queue_ is infinite

        if self._q_capacity and self.size() == self._q_capacity:
            return True

        return False
