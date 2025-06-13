# from itertools import count
#
# f = open('MyData', 'r')
# print(f.read())
# print(f.readline())
# print(f.readline())
#
# f1 = open("abc", 'a')    #a will append and w will overwrite
# f1.write("I am good")

#------🎯 Challenge--------
#-------------- Count word frequencies in a text file----------

from collections import Counter
from itertools import count

f = open('MyData', 'r')
text = f.read()
words = text.split()
result = Counter(words)
for r in result:
    print(f'{result[r]} times {r}')