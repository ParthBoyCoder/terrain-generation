import random

x = 50
y = 60

grassP = 35
dirtP = 20
waterP = 45

for i in range (y):
    for i in range(x):
        list = [0]*grassP + [1]*dirtP + [2]*waterP
        r = random.randint(0,2)
        if (r == 0):
            print("🟩", end="")
        elif (r == 1):
            print("🟫", end="")
        else:
            print("🟦", end="")
    print("")