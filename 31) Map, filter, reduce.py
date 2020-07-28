# Map:- Apply a number on whole list. A function that apply on whole list

# Map function with lambda
def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

# Filter Function
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def greater_5(num):
    return num > 5


gr_than_5 = list(filter(greater_5, list1))
print("These numbers are greater than 5", gr_than_5)

# Reduce function
from functools import reduce

list1 = [1, 2, 3, 4]
num = reduce(lambda x,y:x+y, list1)
print(num)
