def play(money,day_num,allow_gamble):
    import random # Import different files
    import check

    while allow_gamble:
        play = str(input("Start a round(y,n)? (type help for instruction)\n"))
        if play.lower() == "y" or play.lower() == "yes":
            
            if 0 >= money: # Prevent the user from gambling if they do not have money
                print("You do not have money to gamble!\n")
                continue
            
            try: # Prevent the user from enterting floats and limit how much they can gamble
                wager = int(input("How much do you want to wager?(No pennies):\n$"))
            except ValueError:
                print("Invalid Input!\n")
                continue
            if 0 >= wager:
                print("You cannot wager this amount!\n")
                continue
            elif wager > 100:
                print("You wager too much!\n")
                continue
            
            try:
                num_guess = int(input("Guess the number of the dice? (1-6): "))
            except ValueError: # Prevent the user from enterting floats and limit what they can type (between 1 to 6)
                print("Invalid Input!\n")
                continue
            if num_guess >= 7 or num_guess <= 0:
                print("You can't guess this number!\n")
                continue
            
            n = random.randint(1,6) # Determine if the user correctly guess the number (if what they typed is valid)
            if n == num_guess:
                money += wager * 2
                print("Congrats! You won! (+$" + str(wager * 2) + ")\n")
                if random.randint(1,2) == 1:
                    allow_gamble = False
                continue
            else:
                money -= wager
                print("Oops! The number was " + str(n) + "! (-$" + str(wager) + ")\n")
                continue
        
        elif play.lower() == "n" or play.lower() == "no": # Stop the function
            return money, allow_gamble
        
        elif play.lower() == "help": # Display to the user what they can do
            print("\nHow to gamble: You wager money and guess what number the dice is facing upwards\n\ntime: You check what day it is\nwallet: You check how many money you have\n")
            
        elif play.lower() == "time": # Display time
            print(check.time(day_num))
            
        elif play.lower() == "wallet":  # Display how many money the user has
            print(check.wallet(money))
        else: # Prevent unexpected bahviour
            print("Invalid Input!\n")
    else:
        print("You are banned from the casino for this day!\n")
        return money, allow_gamble