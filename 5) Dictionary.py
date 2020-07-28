# Make a dictionary of four words :-
'''print("Enter Your Word")
dict = {"Dog": "Kutta", "House": "Ghar", "Water": "Paani", "Rat": "Chuha"}
dictinpt = input()
print(dict.get(dictinpt))'''

d2 = {"Harry": "Potter", "Aliza": "Beth", "Shivam": {"Burger": "Junk Food", "Chowmein": "Junk Food", "Pizza": "Baked"}}

# Delete Function it is case sensitive
del d2["Harry"]

# Update Function means add a new key in the list
d2.update({"Winters": "Summer"})

print(d2)
# get functions means it gets the value of the given key
print(d2.get("Winters"))

# Print all the key in the list
print(d2.keys())

# Print all the value of the keys
print(d2.values())
