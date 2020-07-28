# Protected class using underscore ( _ )
#  _protect   # Only class or subclass can use this protected class

# Private class uses double underscore ( __ )
#  ___private  # Only user and main class can access this

class Employee:
    no_of_leaves = 8
    var = 50
    _protect = 40
    __pr = 100

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return  f"The name is{self.name} and salary is{self.salary} and role is{self.role}"

    @classmethod
    def change_leaves(cls,newleave):
        cls.no_of_leaves = newleave

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good" + string)


emp = Employee("Shivam Rohilla", 255, "Engineer")
emp1 = Employee.from_dash("Shivam Rohilla-255-Engineer")

print(emp._protect)  # Access Protect class
print(emp._Employee__pr)  # Access private class

print(emp1.name)

print(emp.role)






