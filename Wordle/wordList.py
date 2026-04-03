def get_word(): # Get and return the word for the program
    import random
    wordList = ["quest","curse","swing","found","throw","watch","trice","straw","smite","flout","gawky","march","primo","epoxy","trove"]
    num = random.randint(0,len(wordList)-1)
    return wordList[num]

def get_used_letter(guessed_words): # Get what letters have been used and return them
    used_letter_list = []
    for word in guessed_words:
        word = list(word)
        for letter in word:
            used_letter_list.append(letter) # Add all letters including duplicates
    used_letter_list = list(set(used_letter_list)) # Turn the list into a set to remove all the duplicates, then turn it back to a list and sort it
    used_letter_list.sort()
    return used_letter_list