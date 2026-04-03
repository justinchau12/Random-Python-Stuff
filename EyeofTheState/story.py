def introduction():
    print("\nCongratulations, citizen!\nYou have won the labor lottery.\nYour job is Perception Corrector for the \"Reality of Noristonka\".\nTasks will be deposited each day. Follow rules and filter.\nLong live Noristonka.")
    return

def introduceday(day):
    day_dict = { # Day:Text value pairs
        1:"\n\"Good morning. Welcome to your new job. I am your superior.\"\n\"Work has been deposited. Make no mistakes.\"",
        2:"\n~NEWS~\nReport all Anti-Noristonka terrorists, they might be closer than you think!\n-Loyalty is absolutely required. All citizens who are found aiding terrorism would be prosecuted.\n-Long Live Noristonka\n*a note dropped out of your rulebook*\n\"We are Kriptos.\"\n\"Allow some news about the flu, the people needs to know what the Noristonka government is hiding.\"",
        3:"\n\"They are trying to execute Mr. Houston. We need him.\"\n\"Approve some news about his conditions. We need people to know what is going to happen to him.\"",
        4:"\n~NEWS~\nCitizen of Noristonka, do not join or help anti-Noristonkan collusions!\n\"The secret police is on to us. We cannot talk much.\"\n\"Approve the news with secret code on it.\"\n\"We trust you.\"",
        5:"\n*A note is sticking on your rulebook*\n\"We are at the final step. There will be news about corruption.\"\"Expose them.\"",
        6:"\n~NEWS~\nSome students are marching towards the capital, demanding freedom and the release of political prisoners.\n\"Allow the news about the uprising.\"\n\"More people that knows, the better.\""
    }
    print(day_dict.get(day, "None"))
    return