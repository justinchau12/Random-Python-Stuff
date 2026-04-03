def pig_latin(a,b="",c="",d="",e="",f="",g="",h=""):
    
    word_list = [a,b,c,d,e,f,g,h] # Add all words into word_list and remove empty strings
    word_list = [i for i in word_list if i!=""]
    
    for i,word in enumerate(word_list): # Modify words in word_list to have -ay or -way
        if word[0] not in ["a","e","i","o","u"]:
            word = word[1:] + "-" + word[0] + "ay"
        else:
            word = word + "-" + "way"
        word_list[i] = word
        
    word_list[0] = word_list[0].replace(word_list[0][0], word_list[0][0].upper()) # Make the first word capitalize
    
    sentence = "" # Concatenate all words in word_list as one sentence and a full stop.
    for word in word_list[:-1]:
        sentence += word + " "
    sentence += word_list[-1] + "."
    return sentence

# Driver's code
print(pig_latin("computer", "science", "is", "a", "cool", "subject"))