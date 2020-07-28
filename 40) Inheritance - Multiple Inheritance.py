# Inheritance - Multiple Inheritance
# Use above code and make code reusable or use main class in inherit class or new class
class Employee:
    no_of_leaves = 8
    var = 25

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # def printdetails(self):
    #     return f"Name is {self.name} and salary is {self.salary} or role is {self.role}"

    @classmethod  # This is also called decorator and this function return converted class method.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        #     params = string.split("-")
        #     print(params)
        # return (params[0], params[1], params[2])
        return cls(*string.split("-"))  # One line Method

    @staticmethod  # this static method used in class because we want to print this in only that particular class
    def printgood(string):
        print("This side is " + string)
        # return 2


class Player:
    var = 18
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"name of player is {self.name} and game is {self.game}"


class coolprogrammer(Player, Employee):
    language = "c++"

    def printlanguage(self):
        print(self.language)


shubham = Player("Shubham-Player", ["cricket"])
karan = coolprogrammer("karan", ["hockey"])

det = karan.printdetails()
karan.printlanguage()
print(det)
print(shubham.var)
