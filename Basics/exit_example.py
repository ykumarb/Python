# Import needed modules
import sys

# Exit in action
while True:
    print(f'Enter something ')
    typed = input()

    if typed == "exit":
        sys.exit()
    print("You typed, " + typed)    