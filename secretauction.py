# Secret Auction Program

from art import logo
from os import system


def cls():
    system('cls')


print(logo)
print('Welcome to the secret auction program.')

# Create an Empty Dict
bids = []
continue_bid = True


# Create a Function that adds items to the Dict
def add_bidders(bidder, bid_amount):
    bid_dict = {'Name': bidder, 'Amount': bid_amount, }
    bids.append(bid_dict)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''

    for index in range(len(bidding_record)):
        bid_amount = bidding_record[index]['Amount']
        bidder_name = bidding_record[index]['Name']

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder_name

    print(f'The winner is {winner} with a bid of ${highest_bid}')


while continue_bid:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))

    add_bidders(bidder=name, bid_amount=bid)

    print('Thank You For Your Bid, It has been Saved!')
    other_bidders = input('Are there other bidders? Type \'yes\' or \'no\' ')

    if other_bidders == 'yes':
        cls()

    elif other_bidders == 'no':
        continue_bid = False
        find_highest_bidder(bidding_record=bids)
