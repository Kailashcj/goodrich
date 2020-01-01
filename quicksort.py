#!/bin/python

def qsort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return qsort(less) + [pivot] + qsort(greater)


if __name__=='__main__':
  user_list = list(map(int, input().strip().split()))
  print(qsort(user_list))

