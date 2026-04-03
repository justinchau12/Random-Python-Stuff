import os, work, story

icon = open("icon.txt").read().splitlines() # icon
for line in icon:
    print(line)

print("\nEye of The State\nPress enter to start") # start menu
input("")
os.system('clear')

story.introduction()  # introduction
input("")
os.system('clear')

game = True
day = 1 # In game days
support = 0 # Support decides the ending of the game
credit = 50 # In game currency

while game:
    story.introduceday(day) # print the story at the start of each day
    input("")
    os.system('clear')
    credit, support = work.working(work.pack_work(day),day,credit,support) # work.working requires four parameters; work, day, credit and support
    if day >= 6: # last game day
        if support <= 3:
            os.system('clear')
            print("\nThe protest is over.\nAs for you, officer, we looked at your profile.\nYou excels at your job.\nYour work would be praised on the news.\nGlory to Noristonka, Officer.") # the player not coorperating with Kriptos
            exit()
        elif 4 <= support and support <= 6:
            os.system('clear')
            print("\nThe disturbance is over.\nAs for you, officer, we looked at your profile.\nAlthough there were some mistakes, we can overlook that.\nGlory to Noristonka, Officer.") # the player did not help Kriptos enough
            exit()
        elif 7 <= support:
            os.system('clear')
            print("\nThe tyranny was overthrown.\nNoristonka now truly belongs to the Noristonkans.\nYour job as a Perception Corrector is no longer required.\nYou will now be helping us rebuild Noristonka.\nGlory to New Noristonka.") # the player helped Kriptos
            exit()
    if credit <= 0: 
        os.system('clear')
        print("\nYour work was unsatisfactory.\nNoristonka has zero torlerance for defects.\nThe penalty is forced hard labor.\nYou would be easily replaced.\nLong live Noristonka.") # the player has negative credits
        exit()
            
    else:
        day += 1 # day continues
        os.system('clear')

if not game: # Error handling
    print("Something has gone wrong.")