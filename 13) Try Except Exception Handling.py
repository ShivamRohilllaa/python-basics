num1 = input("Enter first number 1\n")
num2 = input("Enter Second number 1\n")
try:
    print("The Sum of these two numbers is", int(num1+num2))
except Exception as e:
    print(e)
    print("This line is very important")
