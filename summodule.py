def myfun(str):
    return (f"This side is {str}")


def sum(a, b):
    return a + b + 5


# print("Name of Module is", __name__)

if __name__ == '__main__':
    print(myfun("Shivam"))

    i = sum(4,6)
    print(i)
