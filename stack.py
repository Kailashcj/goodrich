#!/bin/python

class Empty(Exception):
    """Error from an empty list"""
    pass

class ArrayStack:
  """LIFO Stack implementation using python list"""
  
  def __init__(self):
    """constructor"""
    self._data = []  # empty stack at the begining

  def __len__(self):
    """return number of elements in stack"""
    return len(self._data)

  def is_empty(self):
    """check if stack is empty"""
    return len(self._data) == 0  # good style, returns true if 0 else returns false

  def push(self, e):
    """push an element into the list"""
    self._data.append(e)

  def pop(self):
    """remove an element from the top of stack"""
    if self.is_empty():
      raise Empty("stack is empty")
    return self._data.pop()

  def top(self):
    """ return the value of top element in stack"""
    if self.is_empty():
      raise Empty("stack is empty")
    return self._data[-1]

if __name__=='__main__':
  s = ArrayStack()
  s.push(5)
  s.push(3)
  print(len(s))
  print(s.pop())
  print(s.is_empty())
  print(s.pop())
  print(s.is_empty())
  s.push(7)
  s.push(9)
  print(s.top())
  s.push(4)
  print(len(s))
  print(s.pop())
  s.push(6)
