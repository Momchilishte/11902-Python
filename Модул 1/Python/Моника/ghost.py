import random

ghost_door = random.randint(1, 4)
ghost_door2 = random.randint(1, 4)
print("There are 4 doors. 2 ghosts aree hiding behind two of them. Can you guess the right one without a ghost? If you find a ghost, you lose, but if you open the right door, you win!")
guess = int(input("Enter a number between 1 and 4"))
if guess != ghost_door:
    print("you win!")
else:
    print("you lose!")