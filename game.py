import random
player = 0
computer = 0
while True:
    pc = random.randint(1, 4)
    pl = int(input())
    if pc > pl:
        computer += 1
        print("PC Won! Scorred  :", computer)
    elif pl > pc:
        player += 1
        print("Player Won! Scorred :", player)
    elif pl == pc:
        pass
        print("A Draw")
