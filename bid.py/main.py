# #The goal is to build a blind auction program.


# import art
# print(art.logo)

# def maxi(players_max):
#     max = 0
#     winner = ""
#     for letter in players_max:
#         marks = players_max[letter]

#         if marks > max:
#             max = marks
#             winner = letter


#         print(f"the winner is {winner} with bid of ${max}")
            





# game_continues = True
# while game_continues:
#     names = input("enter your name ")
#     bid = int(input("Enter your bid in $"))
#     players_play = input("Are there any bidder type 'yes' or 'no'\n")

#     players = {}


#     players[names] = bid
#     if players_play == 'no':
#         game_continues = False
#         maxi(players)

        

#     elif players_play == 'yes':

#         print("\n" * 100)
        
        
           






from art import logo
print(logo)

def find_highest_bidder(bids):
    """
    Finds the highest bidder from a dictionary of bids and prints the winner.

    Args:
        bids (dict): A dictionary where the keys are bidder names and the values are their bids.

    Returns:
        None
    """
    highest_bid = 0
    highest_bidder = ""
    
    # Iterate through the bids to find the highest bid
    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
            
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# Initialize the game loop
game_continues = True
# Dictionary to store all players and their bids
players = {}

# Start the game loop
while game_continues:
    # Get the bidder's name
    name = input("Enter your name: ")
    
    # Get the bidder's bid
    bid = int(input("Enter your bid in $: "))
    
    # Store the name and bid in the players dictionary
    players[name] = bid
    
    # Ask if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    # If there are no more bidders, find the highest bidder and end the game loop
    if should_continue == 'no':
        game_continues = False
        find_highest_bidder(players)
    
    # If there are more bidders, clear the screen and continue the game loop
    elif should_continue == 'yes':
        print("\n" * 100)  # Clear the screen
    else:
        print("Please enter 'yes' or 'no'.")  # Handle invalid input