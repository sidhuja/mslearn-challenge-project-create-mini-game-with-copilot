import random

def get_user_input():
    while True:
        user_input = input("Type rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid input, please try again.")

def determine_winner(user_input, computer_input):
    if user_input == computer_input:
        return "Tie"
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        return "You win"
    else:
        return "You lose"

def play_game():
    score = {"win": 0, "lose": 0, "tie": 0}
    play_again = "yes"
    
    while play_again == "yes":
        user_input = get_user_input()
        computer_input = random.choice(["rock", "paper", "scissors"])
        
        result = determine_winner(user_input, computer_input)
        print(result)
        
        score[result.split()[1]] += 1
        
        print(f"Computer chose {computer_input}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
    
    print(f"Final score: Win - {score['win']}, Lose - {score['lose']}, Tie - {score['tie']}")

play_game()
