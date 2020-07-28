# Star Pattern Program
inp = int(input("Enter The No. of rows\n"))
row = 0
while row < inp:
    star = row+1
    while star > 0:
          print("*", end=" ")
          star = star-1
    row = row+1
    print()
