#!/usr/bin/env python

num = int(input("Input a positive number:"))


def fibonacci(n):
  #complete the recursive function
  if n <= 1 :
    result = 0
    return result
  if n == 2:
    result = 1
    return result
  else:
    result = fibonacci(n-2) + fibonacci(n-1)
    return result

for x in range(num+1):
  if x == 0:
    continue
  else:
    print(fibonacci(x))

fibonacci(num)
