# Class Method
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # def printdetails(self):
    #     return f"Name is {self.name} and salary is {self.salary} or role is {self.role}"

    @classmethod  # This is also called decorator and this function return converted class method.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


shivam = Employee("Shivam Rohilla", "600k/Mo", "Software Engineer")
rohan = Employee("Rohan", "100k/Mo", "Engineer")


rohan.change_leaves(24)
print(rohan.no_of_leaves)

# print(rohan.salary)
