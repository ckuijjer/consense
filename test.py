# -*- coding: utf-8 -*-
import sys

def add(x, y):
  result = x + y
  return sys.stdout.write(str(result))

if __name__ == '__main__':
add(2, 5)