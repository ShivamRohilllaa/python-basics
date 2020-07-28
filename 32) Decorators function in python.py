# Decorators:- This function is used for modify the functionality of function

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

@dec1

def who_is_shivam():
    print("Shivam is a good boy")

who_is_shivam()









