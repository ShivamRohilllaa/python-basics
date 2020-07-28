# Factorial using Iterative Method
# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
#
#
# inp = int(input("Enter the number\n"))
# print("Factorial using Iterative Method", factorial_iterative(inp))


# Factorial using Iterative Method
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
#
#
# inp = int(input("Enter the number\n"))
# print("Factorial using Iterative Method", factorial_recursive(inp))

# Factorial using fibonacci Method

def factorial_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)


inp = int(input("Enter the number\n"))
print("Factorial using fibonacci Method", factorial_fibonacci(inp))



