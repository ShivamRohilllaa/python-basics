# Self
class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"Name is {self.name} and salary is {self.salary} or role is {self.role}"


shivam = Employee()

shivam.name = "Shivam Rohilla"
shivam.salary = "500k/Mo"
shivam.role = "Software Engineer"
print(shivam.printdetails())


# __init__ Constructor gives arguments to the object

class Employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


shivam = Employee("Shivam Rohilla", "600k/Mo", "Software Engineer") # These arguments always goes in INIT

print(shivam.salary, shivam.role, shivam.name)
