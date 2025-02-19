# Nicholas Pratt III
# I have Fixed the Dry, not simple code with no docs
import random

# Global vars for coin
head = 0
tail = 1

# Simulate 1 coin flip with 1/2 chance
def coin_flip():
    return random.randint(0, 1)  # Return 0 for heads or 1 for tails

# Flip coin three times
def three_flip():
    flips = [coin_flip() for _ in range(3)]  # List of three coin flips
    return flips.count(head)  # Count occurrences of 0 (heads)

# Determines the winner of the game
def compare_scores(user_score, computer_score):
    print(f"\nUser got {user_score} HEAD(S) to Computer's {computer_score}!")
    if user_score > computer_score:
        print("User Wins!\n")
    elif user_score == computer_score:
        print("It's a Tie!\n")
    else:
        print("Computer Wins!\n")

# Main game control with loop
def main():
    print("Welcome to Doggo's Coin Flip Game! Flip 3 times to see how many heads you can get against the Computer! Good Luck!")

    while True:
        # Player's turn
        user_heads = three_flip()
        # Computer's turn
        comp_heads = three_flip()
        # Compare scores
        compare_scores(user_heads, comp_heads)

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break  # Exit loop if user doesn't want to continue

if __name__ == "__main__":
    main()
