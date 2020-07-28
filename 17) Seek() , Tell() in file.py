# Tell
# f = open("shivam.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
#
# f.close()

# Seek
f = open("shivam.txt")
print(f.readline())
f.seek(3) # It means this start reading the line from 3rd word
print(f.readline())
f.close()
