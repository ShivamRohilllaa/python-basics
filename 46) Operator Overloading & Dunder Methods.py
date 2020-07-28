#  Operator Overloading
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name of employee is{self.name} and salary is{self.salary} or role is{self.role}"

    @classmethod
    def change_leaves(cls, newleave):
        cls.no_of_leaves = newleave

    def __add__(self, other):
        return self.salary + other.salary  # Add the salary

    def __truediv__(self, other):
        return self.salary / other.salary  # Divide the salary

    def __str__(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"

    def __repr__(self):
        return f"Employee('{self.name},{self.salary},{self.role}')"


emp1 = Employee("Shivam Rohilla", 255, "Engineer")
emp2 = Employee("Rohan", 355, "Developer")

print(emp1.printdetails())
print(emp1 + emp2)
print(emp1 / emp2)

print(str(emp1))
print(repr(emp2))