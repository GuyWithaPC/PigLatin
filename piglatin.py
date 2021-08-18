#Pig Latin Translator
import math

VOWELS = "aeiou"
INF = math.inf

def eng_to_pig(word):
    capitalize = word[0].isupper()
    word = word.lower()
    if any([word[0] == vowel for vowel in VOWELS]):
        #this is the case where the word begins with a vowel, and so we return [word] + "yay"
        word = word + "yay"
    else:
        #this is the case where the word
        firstVowel = min([i if word[i] in VOWELS else INF for i in range(len(word))])
        wordStart = word[0:firstVowel]
        wordEnd = word[firstVowel:]
        word = wordEnd + wordStart + "ay"
        if capitalize:
            word = word[0].upper() + word[1:]
    return word

print("Welcome to the Pig Latin converter!")
print("----------")
while True:
    #main loop
    try:
        sentenceIn = input("type a sentence to convert: ")
        print("----------")
        words = sentenceIn.split(" ")
        sentenceOut = " ".join([eng_to_pig(word) for word in words])
        print("translated sentence:",sentenceOut)
        print("----------")
        while True:
            print("Do you want to convert another sentence? (Y/N)")
            again = input().lower()
            if again != "y" and again != "n":
                print("unsupported input.")
                continue
            else:
                again = (again == "y")
                break
        if not again:
            break
        print("----------")
    except IndexError:
        print("no input was collected. Try again!")

print("goodbye!")