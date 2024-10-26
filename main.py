# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

dictionary = {}


def bidding():
    name = input("What is your name? : ")
    bid = input("What is your bid? : $ ")
    print("\n" * 20)
    dictionary[name] = bid


bidding()

while input("Are there any other bidders? 'yes' or 'no'").lower() == "yes":
    bidding()
else:
    max_bid = max(dictionary.values())
    max_name = max(dictionary, key=dictionary.get)
    print(f"The winner is {max_name} with a bid of {max_bid}")

