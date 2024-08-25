import random

title_color = '\033[1;30;47m'
red = '\033[91m'
yellow = '\033[33m'
red_italic = '\033[3;31m'
green_italics = '\033[3;32m'
reset = '\033[0m'

print(f"{title_color}--------------------ROCK-PAPER-SCISSORS--------------------{reset}")

plays = ["rock", "paper", "scissor"]

print(f"{red_italic}Type rock, paper or scissor as per your choice.\nType 'exit' to end the game.{reset}")

print()

print(f"\nLet's start {input("Player Name: ")}.\nGood Luck!")

user_wins = 0
comp_wins = 0

while True:
    print()
    user_play = input("Play: ").lower()
    
    if user_play not in plays:
        if user_play == 'exit':
            print(f"{red}Game over!{reset}")
            break
        print("Invalid input. Please type rock, paper, or scissor.")
        continue

    comp_play = random.choice(plays)
    print(f"Computer: {comp_play}")

    if user_play == comp_play:
        print(f"{red}\nOops! It's a tie.{reset}")
    elif (user_play == "rock" and comp_play == "scissor") or \
         (user_play == "paper" and comp_play == "rock") or \
         (user_play == "scissor" and comp_play == "paper"):
        print(f"{green_italics}\nUser wins!{reset}")
        user_wins += 1
    else:
        print(f"{green_italics}\nComputer wins!{reset}")
        comp_wins += 1

    print(f"\n{yellow}Score{reset} User: {user_wins} | Computer: {comp_wins}")
