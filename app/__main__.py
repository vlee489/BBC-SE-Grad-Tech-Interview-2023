from app.interface import Interface

# Get number of CPU the player wants to play against
num_of_cpus = 0
while True:
    try:
        user_input = input("How many cpus do you want to play with? : ")
        num_of_cpus = int(user_input)
        break
    except ValueError:
        print("What you gave was not a number, try again!")
# Starts the game
print("You're player 1")
Interface(1, num_of_cpus)
