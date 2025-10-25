# Dice program 


# 1. roll the dice (random --> (6,6))
# 2. do yoou want to cont. (Y/N)

import random


def roll_dice():
    # pass

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(f"Your rolled {d1} and {d2}")
    print(f"You rolled a total of: {d1 + d2}")

    # return (die1,die2)

while True:
    # Roll the dice
    roll_dice()

    # answer if you want to continue

    answer = input("Would you like to roll again: press (y/n)").lower().strip()

    if answer == 'n':
        # print("Thanks for playing..")
        break
    elif answer == 'y':
        print("Roll again ..")
        continue
    else:
        print("Invalid input!")
        break

    
print("Thanks for playing.. ")





