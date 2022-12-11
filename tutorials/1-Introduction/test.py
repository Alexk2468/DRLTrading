import random

# Set the starting number of coins for each player
num_coins_A = 1
num_coins_B = 2

# Set the probability of each player winning each round
probability_A = 2/3
probability_B = 1/3

# Set the number of iterations to run the simulation for
num_iterations = 100000

# Initialize a counter to keep track of the number of times Player B loses all of their coins
lose_all_coins_count = 0

# Run the simulation for the specified number of iterations
for i in range(num_iterations):
    # Initialize the number of coins for each player for this iteration
    coins_A = num_coins_A
    coins_B = num_coins_B

    # Keep playing rounds until one player has all of the coins
    while coins_A + coins_B > 0:
        # Flip a coin to determine who wins this round
        flip = random.random()

        # Check if Player A wins this round
        if flip < probability_A:
            # Player A wins, so they gain a coin and Player B loses a coin
            coins_A += 1
            coins_B -= 1
        else:
            # Player B wins, so they gain a coin and Player A loses a coin
            coins_A -= 1
            coins_B += 1

    # Check if Player B lost all of their coins
    if coins_B == 0:
        # Player B lost all of their coins, so increment the counter
        lose_all_coins_count += 1

# Calculate the probability that Player B loses all of their coins
probability = lose_all_coins_count / num_iterations

# Print the probability
print(f"Probability: {probability}")
