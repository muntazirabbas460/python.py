# dict = {
#               "key" : "val",
#               "subjects" : ["jave", "Python", "C"],
#               "topics" : ("dict", "set"),
#               "Country" : "Pakistan",
#               "City" : "Gilgit",
#               "age": 45,
#               "is_adult": True,
#               25 : 34
# }
# print(dict)

# Nested Dictionary

# student = {
#               "name" : "Aslam",
#               "subject" : {
#                             "Urdu" : 99,
#                             "english" : 90,
#                             "java" : 100

#               }
# }
# print(student["subject"]["Urdu"])

# student = {
#               "name" : "Aslam",
#               "subject" : {
#                             "Urdu" : 99,
#                             "english" : 90,
#                             "java" : 100

#               }
# }
# null_dict ={}
# null_dict ["name"] = "sabka"
# print(null_dict)

# Dictionary Methods

# 1-myDict.keys()

# student = {
#               "name" : "Aslam",
#               "subject" : {
#                             "Urdu" : 99,
#                             "english" : 90,
#                             "java" : 100

#               }
# }

# print(len("subject"))

# my_Dict.keys = return all keys
# myDict.values() = return all values
# myDict.items = returns all (val, key) pairs as tuples
# myDicyt.get("key") = Returns the key according to value
# myDict.update(newDict) = inserts the specified items to dictionary

# collection = {"mango", "cherry", 1, 2, 5, 12.5}
# print(len(collection))
# set methods
# set.add(el)

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# print(collection)

# set Union = combines both set values and return new
# set1 = {1, 2, 3}
# set2 = {7, 8, 9}
# print(set1.union(set2))
# set Antersection = gives common vales of both  set values and return new
# set1 = {1, 2, 3}
# set2 = {1, 5, 3}
# print(set1.intersection(set2))

# WAP to store following word meanings in a python dictionary
# dict = {
#               "table" : "a piece of furniture",
#               "facts" : "facts & figures",
#               "cat": "mammal "
# }
# print(dict)

# You are given a list of subjects for students.  Assume one classroom is required for 
# one subject How many clas room are needed by all students

# subjects = {"Python", "Java", "C++", "Python", "Javascript", "Java", "Python",
#             "C++", "C"}
# print(len(subjects))

# marks = {}
# x = int(input("marks phy : "))
# marks.update({"phy  " : x})

# x = int(input("marks CS : "))
# marks.update({"CS " :  x})

# x = int(input("marks math : "))
# marks.update({"Math " : x})

# print(marks)
#  WAP to store the 9 and 9.0 in the set seperately
set = {
              9, "9.0"
}
print(set)