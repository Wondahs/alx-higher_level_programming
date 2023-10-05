#!/usr/bin/python3
def magic_calculation_102(a, b):
  if a < b:
    c = add(a, b)
    for i in range(4, 6):
      c = add(c, i)
    return c
  else:
    return sub(a, b)

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

if __name__ == '__main__':
  a = int(input('Enter a: '))
  b = int(input('Enter b: '))
  result = magic_calculation_102(a, b)
  print(result)
