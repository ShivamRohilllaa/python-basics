import time
initial1 = time.time()
k = 0
while k < 5:
    print("While loop")
    k += 1
    # time.sleep(2)
print("Time of while loop is", time.time()-initial1, "Seconds")

initial2 = time.time()
for i in range(3):
    print("For loop")
print("Time of for loop is", time.time()-initial2, "Seconds")

# Use time sleep function
initial3 = time.time()
k = 0
while k < 5:
    print("While loop")
    k += 1
    time.sleep(2)
print("Time of while loop is", time.time()-initial3, "Seconds")

