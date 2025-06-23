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

# class Stack:
#     def __init__(self):
#         self.container = deque()
#     def push(self, val):
#         self.container.append(val)
#     def pop(self):
#         return  self.container.pop()
#     def peak(self):
#         return self.container[-1]
#     def is_empty(self):
#         return len(self.container)==0
#     def size(self):
#         return len(self.container)
#
# s = Stack()
# s.push(5)
# print(s.peak())       # It will return the last one, it will not remove
# print(s.peak())
# print(s.pop())       # It will return the last one, it will remove.
# print(s.is_empty())
# print(s.size())
# s.push(67)
# s.push(98)
# s.push(88)
# print("-----------------\n",s.peak())
# print(s.is_empty())
# print(s.size())

#--------------**********************---------------------
# Queue (FIFO) - first in first out

# wmt_stock_price_queue = []
# wmt_stock_price_queue.insert(0, 131.10)
# wmt_stock_price_queue.insert(0, 132.12)
# wmt_stock_price_queue.insert(0, 135)
# print(wmt_stock_price_queue)
# print(wmt_stock_price_queue.pop())   # You will see first in first out here -> output will be 131.1
# print(wmt_stock_price_queue.pop())
# print(wmt_stock_price_queue.pop())
#
# from collections import deque
#
# q = deque()
#
# q.appendleft(5)         # So in the stack we were using append here we will be using appendleft
# q.appendleft(4)
# q.appendleft(3)
# q.appendleft(9)
# q.appendleft(10)
# print(q.pop())          # First in first out
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#     def dequeue(self):
#         return  self.buffer.pop()
#     def peak(self):
#         return self.buffer[-1]
#     def is_empty(self):
#         return len(self.buffer)==0
#     def size(self):
#         return len(self.buffer)
#
# pq = Queue()
# pq.enqueue(
#     {
#         'Company':'Wal Mark',
#         'timestamp': '15 apr, 11.01 AM',
#         'Price': 131.10
#     }
# )
# pq.enqueue(
#     {
#         'Company':'Wal Mark',
#         'timestamp': '15 apr, 11.02 AM',
#         'Price': 132
#     }
# )
# pq.enqueue(
#     {
#         'Company':'Wal Mark',
#         'timestamp': '15 apr, 11.03 AM',
#         'Price': 135
#     }
# )
#
# print(f'Size of the Queue : {pq.size()}')
# print(pq.buffer)
# print(pq.dequeue())


