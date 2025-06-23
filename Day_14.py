# Recursion
from idlelib.colorizer import prog_group_name_to_tag
from wsgiref.util import request_uri

# def find_sum(n):
#     if n==1:
#         return  1
#     return n + find_sum(n-1)
#
#0, 1, 1, 2, 3, 5, 8, 13, 21
#0, 1, 2, 3, 4, 5, 6 ,7, 8
# r = find_sum(5)
# print(r)

# def fib(n):
#     if n==0 or n==1:
#         return  n
#     return fib(n-1) + fib(n-2)
#
# r = fib(10)
# print(r)

#-------------🎯 Challenge----------
#------------- Calculate factorial recursively---------------
1,2,3,4,5
def fact(n):
    if n==1 or n==0:   # base condition
        return 1
    return  n * fact(n-1)

r = fact(4)
print(r)
