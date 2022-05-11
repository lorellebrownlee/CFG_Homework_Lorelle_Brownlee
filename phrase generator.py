"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""


def generate_phrase(characters, phrase):

    # #convert strings into lists
    characters_chars = list(characters)
    phrase_chars = list(phrase)
    #create variable to hold the number of items in the phrase that match a value in the list of characters
    returns_true = 0
    
    #for each item in phrase, check if in characters
    #if in characters, remove it from characters and add +1 to value of returns_true
    #loop to check if the next item is in the new shortened characters string
    length = len(phrase_chars)
    for i in range(length):
        
        if phrase_chars[i] in characters_chars:
            characters_chars.remove(phrase_chars[i])
            returns_true = returns_true + 1

        #if not in characters, return false    
        else:
            return False
    #if the number of characters in the phrase with matching characters in the list of 
    #characters is identical to the length of the phrase, return True
    if returns_true == length:
        return True

#driver code    
print(generate_phrase('cbacba', ''))

#output: False
