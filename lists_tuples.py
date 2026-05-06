# Lists are built in data type that stores set of values.
# It can store elements of different data types i,e integer float, boolean, string etc 
# marks = [94.5, 98.6, 99, 40, 45.1]
# print(marks)
# print(type(marks))  

# student = ["Karan", 79.8, "Arjun"]
# print(student)
# print(type(student))

# lists are mutable and string is immutable in Python
# teacher = ["student", 34, "aslam", "akram"]
# print(teacher[0])
# teacher [0] = "ali"
# print(teacher)

# teacher = ["student", 34, "aslam", "akram"]
# print(teacher[1])
# teacher [1] = "janbaz"
# print(teacher)

# teacher = ["student", 34, "aslam", "akram"]
# print(teacher[2])
# teacher [2] = "karam"
# print(teacher)

# Operations in lists

# Append Method
# list = [1, 2, 3, 4, 5, 6]
# list.append(8)
# print(list)

# list = [6, 9, 10, 1, 2, 3, 4, 5]
# print(list.sort())
# print(list)

# list = [6, 9, 10, 1, 2, 3, 4, 5]
# print(list.sort( reverse=True))
# print(list)

# list = [6, 9, 10, 1, 2, 3, 4, 5]
# list.insert(0, 12)
# print(list)

# list = [6, 9, 10, 1, 2, 3, 4, 5]
# list.pop(2)
# print(list)

# tuples are built in data type in python that lets
# us to create the set of values inside it.  It is immutable just like the strings.

# tuple = (1, 2, 4, 8)
# print(tuple [0:2])
# print(type(tuple))

# for sinfle values placed the , for tuple

# WAP to ask the user to enter the names of their three favorite movies
# & store them in a list.
# movies = []
# mov1 = movies.append(input("enter 1st movie : "))
# mov2 = movies.append(input("enter 2nd movie : "))
# mov3 = movies.append(input("enter 3rd movie : "))
# print(movies)

# WAP to check the palindrome

# list1 = ["m", "a", "a", "m"]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1)

# WAP to count the number of students with the "A" grade in the following tuple
# grade = ["C", "A", "B", "D", "A", "A", "G", 4,  4]
# print(grade.count(4))

grade = ["C", "A", "B", "D", "A", "A", "G"]
grade.sort()
print(grade)




