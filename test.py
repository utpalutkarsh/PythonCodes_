def Translator(phrase):
    changed_phrase=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():      #Doesn't change the nature of the letters, just checks for Upper case
                changed_phrase = changed_phrase + "G"
            else :
                changed_phrase = changed_phrase + "g"

        else:
            changed_phrase= changed_phrase+letter
    return changed_phrase


x= input("Enter a phrase :")
print(Translator(x))