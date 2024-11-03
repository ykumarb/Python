# Import required modules for this task if any needed

# For loop in action
i = 0
inf = 10
LIMIT=2000
for i in range(0,inf,2):
    if inf == LIMIT:
        print("break")
        break
    print(inf, i)
    inf += 2