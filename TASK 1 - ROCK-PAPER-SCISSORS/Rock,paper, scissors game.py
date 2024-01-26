import random

def show_message():
    print("Choose between rock,paper or scissors\n")


def instructions():
    print(
        "You are about to play a rock-paper-scissors game with the computer. The computer will randomly choose an answer and the outcome of the game will be displayed after the game."
        "After every round, the scores will keep updating until you exit the game. Enter no to stop the game"
    )
          


def user_input():
    play = input('Enter your choice : ').lower()
    return play


def get_computer_play():
    valid_choices = ["rock", "paper", "scissors"]
    computer_play = random.choice(valid_choices)
    return computer_play


def winner_decider(play, computer_play):
    print(f"\nYou chose: {play}")
    print(f"The computer chose: {computer_play}")

    if play == computer_play:
        print("It's a tie!")
        return "tie"
    elif (play == "rock" and computer_play == "scissors") or (play == "paper" and computer_play == "rock") or (play == "scissors" and computer_play == "paper"):
        print("You win!")
        return "user"
    else:
        print("Computer wins!")
        return "computer"


def game_start():
    your_score = 0
    computer_score = 0


    instructions()

    while True:
        show_message()
        user_choice = user_input()
        computer_choice = get_computer_play()
        result = winner_decider(user_choice, computer_choice)

        if result == "user":
            your_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nYour Score: {your_score} | Computer Score: {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): \n").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game_start()
