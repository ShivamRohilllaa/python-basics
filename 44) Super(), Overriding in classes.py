class A:
    classvar1 = "I am class variable in Class A"

    def __init__(self):
        self.classvar1 = "Instance var in class A"
        self.var1 = "I am variable in Class A"
        self.special = "special"

class B(A):
    classvar1 = " I am class varaible in class B" # Override above Class

    def __init__(self):
        super().__init__() # This enables the constructor A variables
        self.classvar1 = "Instance var in class B"
        self.var1 = "I am in class B"

a = A()
b = B()

print(b.classvar1) # This find the instance variable in class B if instance variable is not found so this
# inherit the instance variable of class A
print(b.classvar1, b.var1, a.special)
print(b.special)

