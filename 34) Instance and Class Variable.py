class Employee:
     no_of_leaves = 8
     pass
shivam = Employee()
rohan = Employee()


shivam.name = "Shivam Rohilla"
shivam.salary = "500k/Mo"
shivam.role = "Software Engineer"

rohan.name = "Rohan"
rohan.salary = "500k/Mo"
rohan.role = "Singer"
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves = 9 # This Instance Variable creates here but it cannot change main property of employee
print(Employee.no_of_leaves)
print(shivam.no_of_leaves)
print(rohan.no_of_leaves)
