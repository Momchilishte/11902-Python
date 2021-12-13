import random

ghost_door = random.randint(1, 3)
print("There are two doors and ghost is hiding behind one of them")
guess = int(input( "Enter a number between 1  and 2"))
if guess != ghost_door:
    print("You win!")
else:
    print("You lose!")