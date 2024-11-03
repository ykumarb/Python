# Import required modules if necessary
import random

# printing random numbers in action
print(f'Random numbers : ')

# variable for random number
rand_num = 0

while True:
    if rand_num == 1:
        break    
    rand_num = random.randint(1,2000)
    print(f'{rand_num}')