# # Modules
# import math
# from calendar import isleap
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.log10(100))
# print(math.floor(2.3))
# print(math.ceil(2.3))
#
# import calendar
#
# print(calendar.month(2025, 7))
# print(isleap(2025))
# print(dir(calendar))

#-----------Self created module in Day_06_moduleCreated using here--------------
# import Day_06_moduleCreated
#
# Tri_Ar = Day_06_moduleCreated.Triangle_Area(4,4)
# print(f'Area of Triangle = {Tri_Ar}')
#
# Sqr_Ar = Day_06_moduleCreated.Sqr_Area(5)
# print(f'Area of square = {Sqr_Ar}')

#----------🎯 Challenge----------
#- ----------Generate a random 8-character password--------------------

import random
import string

charactor = string.ascii_letters + string.digits + string.punctuation
list1 = []

for i in range(8):
    char = random.choice(charactor)
    list1.append(char)

result   = ''.join(list1)
print(result)