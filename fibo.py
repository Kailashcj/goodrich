#!/bin/python3

def fibo(n):
  a,b=0,1
  for x in range(n):
    yield a
    a,b=b,a+b


if __name__=='__main__':
  n=int(input().strip())
  g = fibo(n)
  for x in g:
    print(x)

