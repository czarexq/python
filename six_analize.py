import random

def roll_dice():
    count = 0
    
    for i in range(101):
        roll = random.randint(1,6)

        if roll == 6:
            count += 1
            
    return count

print(roll_dice())