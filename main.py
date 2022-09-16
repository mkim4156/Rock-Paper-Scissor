import random
#Rock Paper Scissor Game

list = ["rock", "paper", "scissors"]

bot = random.choice(list)
player = None

while player not in list:
    player = input("Rock, Paper, or Scissors: ").lower()
if player == bot:
    print("Player: " + player)
    print("Bot: " + bot)
    print("It is a tie! ")
elif player == "rock":
    if bot == "scissors":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Won! ")
    if bot == "paper":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Lost! ")
elif player == "scissors":
    if bot == "paper":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Won! ")
    if bot == "rock":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Lost! ")
elif player == "paper":
    if bot == "scissors":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Lost! ")
    if bot == "rock":
        print("Player: " + player)
        print("Bot: " + bot)
        print("You Won! ")
