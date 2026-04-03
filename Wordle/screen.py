def clear(): # Clear the whole file and write in the initial display
    file = open("screen.txt","w")
    file.write("------WORDLE------\n")
    file.write("Guess a 5-letter word")
    file.close()

def display(): # Display the file line by line
    import os
    os.system('clear')
    file = open("screen.txt","r")
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()

def writeIn(word): # Add the guessed word into the file
    file = open("screen.txt","a")
    file.write("\n" + word)
    file.close()