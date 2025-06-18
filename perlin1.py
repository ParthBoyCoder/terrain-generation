import random

x = 50
y = 60

for i in range (y):
    for i in range(x):
        if (random.randint(0,1)== 0):
            print("🟩", end="")
        else:
            print("🟫", end="")
    print("")
    