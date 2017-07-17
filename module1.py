#!/usr/bin/python
# Filename: module1.py
'''Prints the maximum of two numbers.

The two values must be integers.'''
import sys

def func():
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    print(100)


for i in range(1, 100):
    func()
for item in sys.path:
    print(item)

print(func.__doc__)
print(100)

print(200)