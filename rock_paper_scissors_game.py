import random

# Program Start: Funny
print("Rock, Scissors and Paper game!")

print("Rules:")
print("1. Rock; 2. Scissors; 3. Paper;")

print("Let's start? (Y / N)")

answer = input()

if answer == 'N':
    print("Goodbye!")
    exit()
elif answer == 'Y':
    # Logic of Game
    
    # win - lose - draw
    win = 0
    lose = 0
    draw = 0
    
    while True:
        options = ["rock", "scissors", "paper"]
        computer = random.choice(options)
        player = input("Enter your choice: ")
        if player not in ("rock", "scissors", "paper"):
            print("You miss spelled!")
            continue
        print("Computer's choice:", computer)
        if computer == player:
            print("Draw!")
            draw += 1
        elif player == 'exit':
            print("Goodbye!")
            exit()
        else:
            if (computer == "rock" and player == "scissors") or (computer == "scissors" and player == "paper") or (computer == "paper" and player == "rock"):
                print("Computer is Won!")
                lose += 1
            else:
                print("You won!")
                win += 1
        print(f'{win} : {lose} : {draw}')
        print("-" * 25)
else:
    print("Please try again!")
