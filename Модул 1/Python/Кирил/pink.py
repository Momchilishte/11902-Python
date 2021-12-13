import random

ghost_door = random.randint(1, 4)
ghost_door2 = random.randint(1, 4)
print("there are three doors,one ove dem hides a ghost")
set = int(input("enter a number 1-4"))

if set != ghost_door:
   print("YU win")
else:
   print("yu lose")
