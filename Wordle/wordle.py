def five_letter_word_check(guess, secret): # Check how well the word that the user guessed correspond to the secret word
    word = ""
    for i in range(len(guess)):
        letter = guess[i]
        if guess[i] == secret[i]: # Correct placement and letter, green
            word += "\033[1;30;42m" + guess[i].upper()
        elif guess[i] in secret: # Correct letter, yellow
            word += "\033[1;30;43m" + guess[i].upper()
        else: # Letter not in the secret word (secret), grey
            word += "\033[1;30;47m" + guess[i].upper()
    word += "\033[0;39;49m" + " " # Need the extra space or the color will contaminate other texts
    return word