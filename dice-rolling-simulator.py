import random
print("Welcome to the Dice Rolling simulator\nDo you want to roll a dice?(Y/N)")
roll = str(input(": "))
while roll == "Y":
    dice = random.randint(1,6)
    print("You Rolled a "+str(dice))
    roll = str(input("Roll again?(Y/N): "))
print("Thanks for using this dice simulator")
