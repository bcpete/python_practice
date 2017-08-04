import random

list_of_choices = ["Rock", "Paper", "Scissors"]

your_wins = 0
comp_wins = 0
num_of_rounds = int(input("What do you want to play to? Best of: 5, 7, 9, etc."))
while((your_wins or comp_wins) < num_of_rounds*.5):
        player_choice = input("Rock, Paper, or Scissors?")
        comp_choice = random.choice(list_of_choices)

        if(player_choice.lower() == comp_choice.lower()):
            print("Tie")
        elif(player_choice.lower() == "rock"):
            if(comp_choice.lower() == "paper"):
                print("You lose")
                comp_wins +=1
            elif(comp_choice.lower() == "scissors"):
                print("You win")
                your_wins+=1
        elif(player_choice.lower() == "paper"):
            if(comp_choice.lower() == "scissors"):
                print("You lose")
                comp_wins +=1
            elif(comp_choice.lower() == "rock"):
                print("You win")
                your_wins+=1
        elif(player_choice.lower() == "scissors"):
            if(comp_choice.lower() == "rock"):
                print("You lose")
                comp_wins +=1
            elif(comp_choice.lower() == "paper"):
                print("You win")
                your_wins+=1
if(your_wins > num_of_rounds*.5):
    print("You won!!! :D")
    print("Your wins: ", your_wins)
    print("comp wins: ", comp_wins)
else:
    print("You lost :(((")
    print("Your wins: ", your_wins)
    print("comp wins: ", comp_wins)
