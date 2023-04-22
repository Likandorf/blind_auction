from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
winning_person = ""
highest_bid = 0
auction = {}
continue_game = True
print(logo)
while continue_game:
  print("Welcome to the blind bid!")
  name = input("What is your name? ")
  bid = int(input("How much will you bid? $"))
  auction[name] = bid
  next_bid = input("Are there any other bidders? Type 'yes' or 'no'  ")
  if next_bid == "no":
    continue_game = False
    for person in auction:
      bid_amount = auction[person]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winning_person = person
  clear()
print(f"The winner is {winning_person} with a bid of ${highest_bid}")
