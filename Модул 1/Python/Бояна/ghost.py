import random

ghost_door = random.randint(1, 3)
ghost_door2 = random.randint(1, 3)
print("There are three doors.A ghost is hiding bening one")
guess = int(input("Enter a number betweem 1 and 3"))
if guess == ghost_door & guess != ghost_door2
    print("You win!")
else:
    print("You lose!")

