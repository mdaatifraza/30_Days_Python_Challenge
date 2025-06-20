# Stack (LIFO) - Last in First Out
# In Python, although a list can be used as a stack (using append() and pop()),
# it is not the most efficient choice for all use cases. This is because Python lists are
# implemented as dynamic arrays.
# When the list exceeds its current capacity (e.g., after adding the 11th element to a list with a
# capacity of 10), Python internally allocates a new larger array (usually doubling the size), copies
# the existing elements, and then adds the new one.
# This resizing process can be expensive in terms of memory and performance.
# So, for stack operations (especially if you are doing a lot of append and pop from the end), it is
# better to use collections.deque, which is optimized for fast appends and pops from both ends.
import socket
from collections import deque


# s = []
# s.append('https://www.aninews.in/')
# s.append('https://www.aninews.in/category/world/')
# s.append('https://www.aninews.in/category/world/asia/')
# print(s.pop())
# print(s.pop())
# print(s.pop())

# from collections import deque
# stack = deque()
# stack.append('https://www.aninews.in/')
# stack.append('https://www.aninews.in/category/world/')
# stack.append('https://www.aninews.in/category/world/asia/')
# print(stack)
#
# print(stack.pop())   # it will take out the last limit form deque.

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return  self.container.pop()
    def peak(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
print(s.peak())       # It will return the last one, it will not remove
print(s.peak())
print(s.pop())       # It will return the last one, it will remove.
print(s.is_empty())
print(s.size())
s.push(67)
s.push(98)
s.push(88)
print("-----------------\n",s.peak())
print(s.is_empty())
print(s.size())