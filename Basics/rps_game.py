# Import the required modules needed if there are any
import random
import sys

# Rock, Paper, Scissor Game in Action

# Global variables to track the game status
ties = 0
wins = 0 
loss = 0

# Have a game loop and player loop and processs

# Print the heading
print("ROCK, PAPER, SCISSOR")

while True: # Main Game loop
    print("%s Wins, %s Losses, %s Ties" % (ties, wins, loss))
    while True: # Player Loop
        print("Enter your move : (r)ock, (p)aper, (s)cissors, (q)uit")
        player_move = input()
        if player_move == "q":
            sys.exit() # Exit the entire program
        if player_move == "r" or player_move == "p" or player_move == "s":
            break; # Player presssed valid char and response is stored already to process
        else:
            print("Type one of 'r', 'p', 's' or 'q'")
    
    # Display player's move
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSOR versus...")

    # Generate and process Computer response at a given instant
    random_num = random.randint(1, 3)

    # Display computer response results
    if random_num == 1:
        computer_move = 'r'
        print("ROCK")
    elif random_num == 2:
        computer_move = 'p'
        print("PAPER")
    elif random_num == 3:
        computer_move = 's'
        print("SCISSOR")

    # Process and Display the game statistics to user game window
    if player_move == computer_move:
        status = "tie"
        ties += 1
    if player_move == 'r' and computer_move == 'p':
        status = "win"
        wins += 1
    if player_move == 'r' and computer_move == 's':
        status = "win"
        wins += 1
    if player_move == 'p' and computer_move == 'r':
        status = "loss"
        loss += 1
    if player_move == 'p' and computer_move == 's':
        status = "loss"
        loss += 1
    if player_move == 's' and computer_move == 'r':
        status = "loss"
        loss += 1
    if player_move == 's' and computer_move == 'p':
        status = "win"
        wins += 1

    if status != "tie": print(f'You {status}')
    else: print(f'Its a {status}')