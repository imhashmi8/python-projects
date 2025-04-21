import art
print(art.logo)

# Empty Bidder List
bidder_list = {}

#Function to add bidders name in Dictionaries
def bid(name, amount):
    bidder_list[name] = amount


# Condition for adding new bidders until they type "No"
number_of_bidder = True


while number_of_bidder:
    bidder_name = input("Enter your Name : ")
    bidder_amount = int(input("Enter the Bid amount in $ : "))
    bid(name=bidder_name, amount=bidder_amount)

    add_new_bidder = input("Type 'Yes' to add new Bidder or 'No' to exit : ").lower()
    if add_new_bidder == "yes":
        print("\n" * 100)
    else:
        number_of_bidder = False


# Checking who is winner of Bidding Action
winner = ""
highest_bid = 0

for bidders in bidder_list:
    bid_amount = bidder_list[bidders]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidders

# Final result
print(f"The winner is {winner} with bid amount of ${highest_bid}")