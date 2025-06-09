# Dictionary

d = {"tom": 1354646, "joe":5353422, "bob":8238943}
print(d)

r1 = d["tom"]
print(r1)

d["sam"] = 77777777

print(d)         # In dic order doesn't matter
del d["sam"]
print(d)

# using for loops
# for key in d:
#     print("key :", key, "values :", d[key])
#or
for k, v in d.items():
    print("Key: ", k, "Values: ", v)

print("tom" in d)

d.clear()         # It will empty the dictionary
print(d)


#-------------------------------------------------------------------------------------------------------
# ✔️ List

courses = ["History", "Math", "Science", "Com_Science"]
courses2 = ["Art", "Education"]
print(courses)

courses.append("Geo")  #added to the end
print(courses)

# courses.insert(0, "pol")  #At specific index position
# print(courses)

# courses.insert(0, courses2)  #inset the 2nd list at starting by giving index position
# print(courses)

courses.extend(courses2)   #it will be added at the end
print(courses)

#If we used append here the complete list will be added with [].
# courses.append(courses2)
# print(courses)

# courses.remove("Education")
courses.pop() #By default remove last value, also if want to store pop out value then this is used.
print(courses)

# courses.reverse()
print(courses)

num = [1,2,3,4,5,6]
print(max(num))
print(sum(num))

#find the values position in the list
print(courses.index("History"))
print("History" in courses) #Return true or false

# for item in courses:
#     print(item)         # Print each one in the new line

for index, item in enumerate(courses):
    print(index, item)         #To get both index and value

course_str = ', '.join(courses)   # commas separate
print(course_str)             #History, Math, Science, Com_Science, Geo, Art

new_list = course_str.split(', ')   # back to the list
print(course_str)
print(new_list)

#List is Mutable ( means values can be changed)

List1 = ["History", "Math", "Science"]

List2 = List1
print(List1)
print(List2)

List1[0] =  "Art"
print(List1)
print(List2)

#-----------------------------------------------------------------------------------------------------
# Tuple is Immutable
# Tuple is same as List just use small bracket instead square bracket
point = (5, 9) # 5 represent as x co-ordinate and 9 as y co-ordinate.
print(point[1]) # Same as List
# List is homogenous but the Tuple is heterogeneous

tuple1 = ("History", "Math", "Science")

tuple2 = tuple1
print(tuple1)
print(tuple2)

# tuple1[0] =  "Art"        # If we try to run this part then we will get an error
# print(List1)
# print(List2)

#-----------------------------------------------------------------------------------------------------

#Set ( are un-ordered and unique values)
print("now for sets----------------")
set = {"History", "Science"}  #At each run the order of the value get changed
print(set)  # If we add duplicated values then only one value will be printed

set2 = {"History", "Math", "Science", "Physics"}
print(set.intersection(set2))  # It will return the common values in both the sets
print(set.difference(set2))    #what is in set but NOT in set2. so it will return nothing
print(set2.difference(set))
print(set.union(set2))           # add both the sets


# #Empty list
# empty_list = []
# empty_list = list()
#
# #Empty tuple
# empty_tuple = ()
# empty_tuple = tuple()
#
# #Empty sets
# emptly_set = {} #this is not the correct because it will create list
# empty_set = set() # Correct way