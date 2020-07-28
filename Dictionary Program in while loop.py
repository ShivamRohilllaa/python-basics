while (True):
    print("Enter Your word")
    dict1 = {"Cat": "Pussy", "Bat": "Vampire", "Dog": "Bark", "Hat": "Cap"}
    inp = input()
    if inp in dict1:
        print(dict1.get(inp))
        break
    else:
        continue

