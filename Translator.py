def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #checks if letter is a vowel
            if letter.isupper():
                translation+="G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


print(translate("Adithya Swaminathan"))