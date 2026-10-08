import random 

print("welcome to the rock paper scissors game!!\n")
user = input("enter your choice (rock/paper/scissors): ")

def computer_choice():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

choice = computer_choice()
print(f"computer's choice is: {choice}")

if user == choice:
        print("its a tie!!")
elif user == "rock" and choice == "scissors":
        print("you win!!")
elif user == "paper" and choice == "rock":
        print("you win!!")
elif user == "scissors" and choice == "paper":
        print("you win!!")
else:
        print("you lose!!")


