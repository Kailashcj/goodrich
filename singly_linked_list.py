#!/bin/python

class Empty(Exception):
  """Empty exception class"""
  pass

class LinkedStack:
  """ LIFO stack implementation using a singly linked list"""

  class _Node: # nested class as its only being used by LinkedStack class
    """non-public class for storing a linked list node"""
   # __slots__ = '_element', '_next' # __slots__ is python in-built type for faster attribute access and memory saving
                                    #  

    def __init__(self, element, mynext):
      self._element = element
      self._next = mynext

  # stack methods

  def __init__(self):
    """create an empty stack"""
    self._head = None
    self._size = 0

  def __len__(self):
    """return number of elements in the stack"""
    return self._size

  def is_empty(self):
    """check for empty stack"""
    return self._size == 0

  def push(self, e):
    """insert an element at the head of the list"""
    self._head = self._Node(e, self._head) # create and link a new node
    self._size += 1

  def top(self):
    """return the head element"""
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element

  def pop(self):
    """remove and return the element from the top of the stack"""
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    return answer


if __name__=='__main__':
    s = LinkedStack()
    for i in range(10):
        s.push(i)
    print(s.top())
    print(len(s))
    s.pop()
    print(s.top())
    print(len(s))
    middle = 0
    tail = len(s) - 1
    curr = s._head
    while tail > 0:
      print(curr)
      curr = curr._next
      tail -= 1
      print(tail,':',curr._element)
