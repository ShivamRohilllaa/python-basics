f = open("shivam.txt", "w")
f.write("Writing and append and add some content in the file\nShivam ")
f.close()

# Count how many words you wrote in the file
f = open("shivam.txt", "w")
a = f.write("Hello\n")
print(a)
f.close()

# Handle read and write both
f = open("shivam.txt", "r+")
print(f.read())
f.write("Shivam Rohilla")