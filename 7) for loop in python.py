# Use for loop in dictionary

"""list1 = ["Shivam", "Rohilla", "Shubham", "Harry"]
for item in list1:
    print(item)"""

# List in List
"""list2 = [["Shivam", 20], ["Rohilla", 21], ["Shubham", 25], ["Harry", 30]]
for item, age in list2:
    print(item, age)
"""
# Use for loop in dictionary
list1 = [["Shivam", 20], ["Rohilla", 21], ["Shubham", 25], ["Harry", 30]]
dict1 = dict(list1)
for item, age in dict1.items():
    print(item, "and age is", age)