def time(day_num): # Arrange on displaying the day
    return "\nDay " + str(day_num) + "\n"

def wallet(money): # Arrange on displaying the money
    return "\nYou have $" + str(money) + ".\n"

def end(money, day_num, bill): # Find and return the suitable final comment
    print("\nFinal comment:\n")
    if 0 >= money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. Probably shouldn't have gambled, huh?"
    elif 300 - bill[-1] == money or 300 == money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. Did you even do anything at all?"
    elif 300 > money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. Please stop gambling your live savings."
    elif 500 >= money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. I know you've actually won some \"money\" but please don't actually try gambling in real life."
    elif 1000 >= money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. You are either an experienced gambler or just insanely lucky. But please bear in mind gambling is not the way to live"
    elif 10000 >= money:
        return "You have $" + str(money) + " after " + str(day_num - 1) + " day(s) of gambling. WHAT IN THE WORLD??? You either outsmarted the system or you are just straight up cheating, please touch grass."
    else:
        return "ERROR"

def pay(): # Calculate how much the user needs to pay and returns it
    food = 30
    rent = 15
    water_elec = 10
    total = 0
    bill_name = ["Food", "Rent", "Water & Electricity","Total"]
    bill = [food, rent, water_elec]
    for i in bill:
        total += i
    bill.append(total)
    return bill_name, bill
    
def beg(money): # Generate a random number and add it to money in respect of how much the user has
    import random
    if 50 <= money:
        return random.randint(4,23)
    elif 0 <= money:
        return  random.randint(7,26)
    else:
        return random.randint(10,29)
        
def event(event_name,money): # Generate random event
    import random
    if event_name == "gamble" and money >= 35:
        if random.randint(1,10) == 1: ## Please change the percentage
            return True
    elif event_name == "wallet" and money >= 15:
        if random.randint(1,5) == 1:
            return True
    return False