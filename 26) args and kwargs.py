# def funargs(*args):
#     print(args[0])
#
# Shivam = ["Chowmein/Noodles", "Momos", "Burger", "Pizza"]
# funargs(*Shivam)

# Use for loop for print


# def funargs(*args):
#     for item in args:
#         print(item)
# Shivam = ["Chowmein/Noodles", "Momos", "Burger", "Pizza"]
# print(*Shivam)

# Imp Sequence normal, *args, **kwargs

def funargs(normal, *argsshiv, **kwargsshiv):
    print(normal)
    for item in argsshiv:
        print(item)
    for key, value in kwargsshiv.items():
        print(f"My name is {key} and my hobby is {value}")


ar = ["Shivam", "Rohan", "Puneet", "Vikas"]

normal = "My name is shivam and i would like to represent these:"

kw = {"Shivam": "fitness trainer", "Rohan": "Rapper", "Puneet": "Air Force", "Vikas": "BussinessMan"}
funargs(normal, *ar, **kw)
