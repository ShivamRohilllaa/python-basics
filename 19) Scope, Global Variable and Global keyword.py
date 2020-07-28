# i=10 # This is global variable
#
# def function1():
#     l = 5 # Local Variable
#     m = 8 # Local Variable
#     l = l + 45
#     print(l, m)
#
# function1()
#
# print(i)

# Use global keyword

a = 90


def function1():
    b = 20

    def function2():  # Nested List
        global a  # Now this is global variable
        a = 60

    function2()
    print("This is f2", a)


function1()
print(a)
