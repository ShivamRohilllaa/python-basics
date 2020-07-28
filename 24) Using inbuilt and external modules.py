# In this we using python inbuilt and external modules and using import function

import random
# random_number = random.randint(0,1) # random number print b/w 0 or 1
# random_number = random.randint(0,100) # random number print b/w 0 or 100
#
# print(random_number)

rand = random.random() * 100
print(rand)

list = ["Shivam", "a", "b", "z"]
choice = random.choice(list)
print(choice)
