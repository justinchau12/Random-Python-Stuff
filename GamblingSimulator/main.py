print("~~ GAMBLING SIMULATOR ~~")
print("Goal: Gamble until you think it's enough. You have limited action points (A.P.) each day!\n")

while True: # Loops until the user decides to start the game or not
    start = str(input("Start(y,n)?\n"))
    if start.lower() == "y" or start.lower() == "yes":
        print("")
        break
    elif start.lower() == "n" or start.lower() == "no":
        print("\nYou have decided that gambling is not the way to live, so you quit. Hooray!\n")
        exit()
    else:
        print("Invalid Input!\n")

import gamble # Import different files into the main code
import check

# Setting up variables
money = 300 # The amount of cash the user has
bill_name, bill = check.pay() # Determine what user has to pay each day
day_num = 1 # The day the game has elapsed
action_point = 4 # Limit how much the user can do in a day
allow_gamble = True # Limit how much the user can gamble
game = True # Determine if the game is running

while game: # Loops until user loses or quits
    if action_point != 0: # Detect if user has used up all the action points
        action = str(input("What do you want to do? You have " + str(action_point) + " A.P. (type help for instruction)\n"))
    else:
        action = "sleep"
    if action.lower() == "help": # Display to the user what they can do
        print("\ntime: You check what day it is\nwallet: You check how many money you have\nbill: You check what you have to pay at the end of every day\ngamble: You go gambling (-2 A.P.)\nbeg: You beg people to donate to you (-1 A.P.)\nsleep: You sleep to the next day\nquit: You end with all the money you have\n")
        
    elif action.lower() == "time": # Display time
        print(check.time(day_num))
        
    elif action.lower() == "gamble": # Start gambling
        money, allow_gamble = gamble.play(money,day_num,allow_gamble)
        print("(-2 A.P.)")
        if check.event("gamble",money) == True:
            print("\n*Two man just robbed some of your money! (-$35)*")
            money -= 35
        print("")
        action_point -= 2
        
    elif action.lower() == "sleep": # Start a new day or end the game
        day_num += 1
        money -= bill[-1]
        print("\n(-$" + str(bill[-1]) + ")")
        if 0 > money:
            print("\nYou have gone bankrupt!\n")
            game = False
            continue
        else:
            print("\nZZZ~\nIt's Day " + str(day_num) + "!\n")
            action_point = 4
            allow_gamble = True
        
    elif action.lower() == "wallet": # Display how many money the user has
        if check.event("wallet",money) == True:
            print("\n*You discovered some of your money has been stolen! (-$15)*")
            money -= 15
        print(check.wallet(money))

    elif action.lower() == "bill": # Display to the user what they have to pay each day
        print("")
        for i in range(len(bill)):
            print(str(bill_name[i]) + ": $" + str(bill[i]))
        print("")
    
    elif action.lower() == "beg": # Give random amount of money to the user
        if 120 <= money:
            print("\nEverybody thought that you were just pretending to be poor! (-1 A.P.)\n")
        else:
            donate = check.beg(money)
            money += donate
            print("\nSomeone gave you $" + str(donate) + ". You now have $" + str(money) +". (-1 A.P.)\n")
        action_point -= 1
    
    elif action.lower() == "quit": # Stop the loop
        day_num += 1
        money -= bill[-1]
        if 0 > money:
            print("\nYou have gone bankrupt!\n")
        else:
            print("\nYou have decided to stop gambling!\n")
        game = False
    else: # Prevent unexpected bahviour
        print("Invalid Input!\n")

print(check.end(money, day_num, bill)) # Print the final results
exit()