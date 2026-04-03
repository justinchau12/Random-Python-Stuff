import random # Import the random libaray

user_hand = input("Choose Rock, Paper, or Scissors: ") # Get user's input

if user_hand in ["Rock", "Paper", "Scissors"]: # Make sure user enters either Rock, Paper or Scissors
    comp_hand = random.choice(["Rock", "Paper", "Scissors"]) # Randomly choosing computer's choice
    print("The computer chose " + comp_hand + ".")
    
    if user_hand == comp_hand: # Tie if both user and computer chose the same gesture
        print("This is a tie!")
        
    elif user_hand == "Rock": # Determining who wins the game and then output the results
        if comp_hand == "Paper":
            print("Paper beats Rock, the computer wins!")
        elif comp_hand == "Scissors":
            print("Rock beats Scissors, you win!")
    elif user_hand == "Paper":
        if comp_hand == "Rock":
            print("Paper beats Rock, you win!")
        elif comp_hand == "Scissors":
            print("Scissors beats Paper, the computer wins!")
    elif user_hand == "Scissors":
        if comp_hand == "Rock":
            print("Rock beats Scissors, the computer wins!")
        elif comp_hand == "Paper":
            print("Scissors beats Paper, you win!")
else:
    print("Please pick Rock, Paper, or Scissors!") # Tell user to enter the desirable input
