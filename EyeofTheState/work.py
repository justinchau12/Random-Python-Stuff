def working(works,day,credit,support):
    import story
    cite = 0

    for work in works:
        while True: # the gameplay would continue if the player doesn't err for three times
            
            title = work[0] # defining variables
            word = work[1]
            motto = work[2]
            wrongpart = work[3]
            
            print("\nTitle: " + title + "\nText: " + str(word) + "\nMotto: " + motto) # print work
            
            ans = str(input(" Approve or disapprove? y/n (Type book to refer to rulebook): ")) # asking for user input
            
            if ans.lower() in ["yes","y","approve"]: # user approved
                if wrongpart == "title":
                    cite += 1
                    print("CITATION " + str(cite) + ": Article title consists of banned words")
                    credit -= 5
                    print("-5 credits")
                elif wrongpart == "text":
                    cite += 1
                    print("CITATION " + str(cite) + ": Article text consists of banned words")
                    credit -= 5
                    print("-5 credits")
                elif wrongpart == "motto":
                    cite += 1
                    print("CITATION " + str(cite) + ": Article contains wrong motto")
                    credit -= 5
                    print("-5 credits")
                elif wrongpart == "special": # special cases
                    if day == 2:
                        cite += 1
                        print("CITATION " + str(cite) + ": Article contains information of diseases")
                        credit -= 10
                        print("-10 credits")
                        support += 1
                    elif day == 3:
                        cite += 1
                        print("CITATION " + str(cite) + ": Article contains classified details")
                        credit -= 10
                        print("-10 credits")
                        support += 1
                    elif day == 4:
                        support += 1
                    elif day == 5:
                        cite += 1
                        print("CITATION " + str(cite) + ": Article violates authority of Noristonka")
                        credit -= 10
                        print("-10 credits")
                        support += 1
                    elif day == 6:
                        cite += 1
                        print("CITATION " + str(cite) + ": Article is anti-Noristonka")
                        credit -= 10
                        print("-10 credits")
                        support += 1
                break
            
            elif ans.lower() in ["no","n","disapprove"]: # user disapproved
                if wrongpart == "correct":
                    cite += 1
                    print("CITATION " + str(cite) + ": Article does not violate protocols")
                    credit -= 5
                    print("-5 credits")
                break
                    
            elif ans.lower() == "book": # user asked to see the rulebook + note
                print("\nArticle title must not have:\n-Unapproved personal opinions\n-Usage of not, no etc.\nArticle text must not have:\n-Words that promote thinking e.g. wonder,think \n-Usage of negative words\nMotto must be:\n-Present\n-Praise Noristonka and its spirit")
    
    credit += 15
    print("\nToday's work is finished. +15 credits")
    print("Support: " + str(support))
    print("Your credits: " + str(credit))
    input("")            
    
    return credit ,support
    
def pack_work(day):
    import random
    pack_dict = { # Day:[random,scripted] value pairs
        1: [3,0],
        2: [4,2],
        3: [4,2],
        4: [5,2],
        5: [5,2],
        6: [5,2]
    }
    works = [-1] * pack_dict.get(day,"None")[0] # insert works with -1 according to how many work the day needs
    for i in range(len(works)): # replace all -1 with the assign_work function
        works[i] = assign_work(True)
    for i in range(pack_dict[day][1]):
        works.insert(random.randrange(len(works)),assign_work(False,day))
    return works

def assign_work(random_generate,day=0): # Generate/Assign work for the day
    import random
    work = []
    
    wrongtitles = [
    "Wheat production not accord to 3-year plan goal",
    "Lack of books for children in Murstock City",
    "Central Court of Justice lacks transparency in trials",
    "The promoise for revitalization of textile production never accomplished",
    "No clean water supply after 11 days at Barovskha","Teira Kleom was an ally of ours 8 years ago - yet we fight today - Why?",
    "I detest all corrupt government officials",
    "No change means downfall of Noristonka",
    "New infrastructures at Devon are not stable enough",
    "Helps still not here at Rethi after strong blizzard",
    "Starvation is 15% higher compared to last year - how it might affect us",
    "Slow responses to potential natural disasters haunt me",
    "No water supplies after severe drought hits farms of Noristonka"
    ]
    safetitles = [
    "Concrete industry may face new tariffs",
    "Ministry of Culture is set to collaborate with commerical cinemas",
    "Cityhall of Naimey will be demolished to build a new Noristonkan Committee Office",
    "Overlooked ways to work harder",
    "46-year anniversary of Noristonka parade in captital town square",
    "New innovation in tanks",
    "Right of patent declared illegal",
    "How you can be more devoted to the Noristonka",
    "Ancient temple exploded for new factories",
    "New movie \" I was a capitalist for the INO \" received the extinguished media award of Noristonka",
    "Anti-Noristonka terrorists arrested",
    "Wheat production surpassed 3-year plan goal",
    "Proxy of capitalists - Teira Kleom declared war on Noristonka",
    "Devon's 3 housing units constructed under 30 days",
    "Beaware of naysayers of Noristonka - report them to authorities if seen"
    ]
    
    wrongwords = [
    "think","believe","wonder",
    "explain","understand","realise",
    "determine","remember","recall",
    "elaborate","comprehend","remind"
    ]
    safewords = [
    "answer","agree",
    "reserve","assume","admit",
    "approve","instruct","listen",
    "supply","award","compete",
    "value","produce","edit",
    "feature","shiver","perform",
    "account","insert","advance",
    "campaign","build","arrange",
    "relax","courage","medal",
    "accept","arise","assure",
    "promise"
    ]
    
    wrongmotto = [
    "None",
    "I am done with this",
    "Noristonka is brainwashing",
    "Government of Noristonka is ILLEGAL",
    "We can't even decide if we want to write motto or not",
    "A tyranny, that is",
    "We want freedom",
    "No more control",
    "Free us",
    "Press should not be oppressed",
    "Noristonka leads to poverty",
    "Chairman's Noristonka",
    "Revolution of what?"
    ]
    safemotto = [
    "Long Live Noristonka",
    "Glory to Noristonka",
    "Noristonka above all",
    "Noristonka united",
    "People's Noristonka",
    "Endure, Labor, Progress",
    "Noristonka or Death",
    "Be loyal to Noristonka",
    "Noristonka leads to prosperity",
    "Noristonka excels",
    "Revolution of the human race",
    "Advance, comrades!",
    "No step back, Noristonkan!",
    "We watch the sky and rule the ground"
    ]
    
    if random_generate:
        potential_wrongpart = ["title","text","motto","correct","correct","correct"] # determines what part of the news is wrong (adding more correct is to fix the odds)
        wrongpart = random.choice(potential_wrongpart)
        
    else:
        wrongpart = "special" # label for planned news
    
    
    if wrongpart == "title": # wrong title
        work.append(random.choice(wrongtitles))
    else: # correct title
        work.append(random.choice(safetitles))
        
    words = []
    if wrongpart == "text": # wrong text
        for word in range(4):
            words.append(random.choice(safewords))
        words.insert(random.randrange(len(words)),random.choice(wrongwords))
        work.append(words)
    else: # correct text
        for word in range(5):
            words.append(random.choice(safewords))
        work.append(words)
        
    if wrongpart == "motto": # wrong motto
        work.append(random.choice(wrongmotto))
    else: # correct motto
        work.append(random.choice(safemotto))
    
    if wrongpart == "special": # special cases
        if day == 2:
            specialtitles = ["Potential virus outbreak in New Rocktim","Mysterious disappearance of multiple doctors and nurses","Some patients unallowed to leave United Rocktim Hospital","New case of mutanted influenza","Unknown rampage disease near New Rocktim"]
            work[0] = random.choice(specialtitles)
        elif day == 3:
            specialtitles = ["Missing election candidate - where is he now?","Ludolf Houston still in jail","Former election candidate tortued","18 years since Ludolf Houston sentenced in jail for secession and complicity with armed gangs","Trial would be closed for former election runner Ludolf Houston"]
            work[0] = random.choice(specialtitles)
        elif day == 4:
            specialwords = ["agua","monde","unidad","oj","padre","devant","lutte","coraje","segreta","alma","pierre","herbe"]
            work[1][random.randrange(0,len(work[1]))] = random.choice(specialwords) 
        elif day == 5:
            specialtitles = ["Monopolies of high rank offical","Money laundering proofs of chairman of Noristonka commitee","Classified documents shows bribery of military officals","Shortage of bread is caused by unfair market competition"]
            work[0] = random.choice(specialtitles)
        elif day == 6:
            specialtitles = ["Students protest in the capital","Police stationed around the capital, preparing for potential riots","Protests in captial might shake the rule of Noristonka commitee","Entry passes required to enter the capital"]
            work[0] = random.choice(specialtitles)
            slogan = "no more lies"
            sloganvar = slogan[8:] + " " + slogan[0:7]
            slogans = [slogan,sloganvar]
            work[2] = random.choice(slogans)

    work.append(wrongpart) # work would now be the form of [title, [words], motto, wrongpart]

    return work