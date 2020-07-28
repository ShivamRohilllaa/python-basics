# Use with block to open the python file
with open("shivam.txt") as f:
    a = f.readline()
    print(a)

# In 'with' we don't need to use f.close() because it managed by itself

