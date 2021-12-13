import random

ghost_door = random.randint(1, 3)
ghost_door2 = random.randint(1, 3)
print("There are 3 doors. A ghosts is hiding behind one door.")
gh = int(input("Enter a number between 1 and 3"))
if gh != ghost_door2 & gh != ghost_door2:
    print("You win!")
else:
    print("You lose!")

