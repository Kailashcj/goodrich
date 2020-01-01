#!/bin/python

class Scoreboard:
  """Fixed length sequence of high scores"""

  def __init__(self, capacity=10):
    """initialize scoreboard with max capacity"""
    self._board = [None] * capacity  # initialize the list with initial capacity with None entries
    self._n = 0   # number of actual entries

  def __getitem__(self), k:
    """return entry at index k"""
    return self._board[k]

  def __str__(self):
    """string representation of highest score board"""
    return '\n'.join(str(self._board[j]) for j in range(self._n))

  def add(self, entry):
    """add entry to high scores list"""
    score = entry.get_score()

    # Does the new entry qualify for high score ?
    # answer is yes if board is not full or score is higher than last entry

    good = self._n < len(self._board) or score > self._board[-].get_score()

    if good:
      if self._n < len(self._board):
        self._n += 1

        # shift lower scores down
        j = self._n
        while j > 0 and self._board[j - 1].get_score() < score:
          self._board[j] = self._board[j - 1]
          j -= 1
        self._board[j] = entry
