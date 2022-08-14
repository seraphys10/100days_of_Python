import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = {}
continue_flag = True
while continue_flag:
    name = input("What is your name? : ")
    bid = float(input("What's your bid? : $"))
    bidders[name] = bid
    if "no" == input("Are there any other bidders? Type 'yes' or 'no'. \n"):
        continue_flag = False
    os.system("cls")
highest_bid = 0
for k,v in bidders.items():
    if v > highest_bid:
        winner = k
        highest_bid = v
print(f"The winner is {winner} with a bid of ${highest_bid}.")


