import random

user_wins = 0
cpu_wins = 0

while True:
    user_input = input("Type Rock, Paper, Scissors or Done to finish: ").lower()
    if user_input == "done": 
        print("User wins: ", user_wins)
        print("Cpu wins: ", cpu_wins)
        quit()
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please type in a singular word, such as Rock")
        continue

    cpu_input = random.randint(0,2)
    # 0 = Rock, 1 = Paper, 2 = Scissors
    print("test")
    if cpu_input == 0:
        if user_input == "rock":
            print("Tie, try again!")
        elif user_input == "scissors":
            print("Aww, you lost this round.")
            cpu_wins+=1
        else:
            print("You win this round!")
            user_wins+=1
    elif cpu_input == 1:
        if user_input == "paper":
            print("Tie, try again!")
        elif user_input == "rock":
            print("Aww, you lost this round.")
            cpu_wins+=1
        else:
            print("You win this round!")
            user_wins+=1
    elif user_input == "scissors":
        print("Tie, try again!")
    elif user_input == "papper":
        print("Aww, you lost this round.")
        cpu_wins+=1
    else:
        print("You win this round!")
        user_wins+=1
        
