def word(guessed_words): # Set guess as a 5 letter word that only consists letters and repeat until true
    while True:
        guess = str(input())
        print ("\033[A                             \033[A") # Clear the input
        if not guess.isalpha(): # Word has  some numbers or symbols
            print("Word can only consists letters!")
        elif len(guess) != 5: # Word is less or more than 5 characters
            print("Word need to be 5 letters!")
        elif guess in guessed_words: # Word has already been guessed before
            print("The word has alreay been guessed!")
        else:
            return guess

def again(): # Ask user if they want to play again and repeat until they say yes or no
    while True:
        answer = str(input("Play again? (y,n) "))
        if answer not in ["yes","y","no","n"]: # User not answering yes or no
            print("Invalid input!")
        if answer in ["yes","y"]: # User wants to play again
            return True
        if answer in ["no","n"]: # User doesn't want to play again
            return False