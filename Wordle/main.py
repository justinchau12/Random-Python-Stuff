import screen, wordle, wordList, validInput # Import files

play = True

while play: # Initiate main loop

    tries = 5 # Amount of tries the user can guess before losing
    guessed_words = [] # List of words that user guessed
    secret = wordList.get_word() # Set secret as the word
    
    screen.clear() # Prepare to print the file
    screen.display()
    
    for i in range(tries):
        guess = validInput.word(guessed_words) # Word fitted the requirements
        guessed_words.append(guess) # Add the guess word into the list of guessed words
        screen.writeIn(wordle.five_letter_word_check(guess, secret)) # Put the guessed word and its colours into screen.txt
        screen.display()
        print("You have used ",end="") # Print the used letters
        print(wordList.get_used_letter(guessed_words))
        
        if guess == secret: # User guessed the word
            print("------YOU WIN!------")
            play = validInput.again()
            break
    
    else:
        print("------YOU LOST!------") # User failed to guess the word before running out of tries.
        print("The word was " + secret.upper() + ".")
        play = validInput.again()
    
exit()

"""
Notes:
What if there are two same letters in the word e.g. grass, hurry?
Only allow user to type actual english words? e.g traps not wwwtt
"""