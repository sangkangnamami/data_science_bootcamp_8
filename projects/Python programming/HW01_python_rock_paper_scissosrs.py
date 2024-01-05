## HW01 - create game pao ying chub
import random

#count_win = 0
#count_lose = 0
#count_tie = 0

def paoyingchub():
    global count_win, count_lose, count_tie  # Declare variables as global
    count_win = 0
    count_lose = 0
    count_tie = 0
    choice = ["rock", "paper", "scissors"]
    print("This is PAO YING CHUB GAME !!!")
    answer = [] # blank
    while True:
        computer_pick = random.choice(choice)
        user_pick = input("Plese type: rock/paper/scissors (or 'quit' to exit): ")
        answer.append(user_pick)

        if computer_pick == user_pick:
            print("Tie.")
            count_tie += 1
        elif (computer_pick == "rock" and user_pick == "paper"):
            print("You win!")
            count_win += 1
        elif computer_pick == "rock" and user_pick == "scissors":
            print("You lose T^T")
            count_lose += 1
        elif computer_pick == "paper" and user_pick == "scissors":
            print("You win!")
            count_win += 1
        elif computer_pick == "paper" and user_pick == "rock":
            print("You lose T^T")
            count_lose += 1
        elif computer_pick == "scissors" and user_pick == "rock":
            print("You win!")
            count_win += 1
        elif computer_pick == "scissors" and user_pick == "paper":
            print("You lose T^T")
            count_lose += 1
        elif user_pick == "quit":
            print("See you next time.")
            answer.pop(-1)
            print(f"Log: {answer}")
            total_play = len(answer)
            print(f"Total played: {total_play}")
            print(f"Total win: {count_win}")
            print(f"Total lose: {count_lose}")
            print(f"Total tie: {count_tie}")
            break

# run this
paoyingchub()
