import random

x = 50
y = 60

for i in range (y):
    for i in range(x):
        r = random.randint(0,2)
        if (r == 0):
            print("🟩", end="")
        elif (r == 1):
            print("🟫", end="")
        else:
            print("🟦", end="")
    print("")
    