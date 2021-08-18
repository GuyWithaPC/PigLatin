#Pig Latin Translator
import math

VOWELS = "aeiou"
INF = math.inf

def pig_to_eng(word,capitalize):
    word = word.lower()
    if any([word[0] == vowel for vowel in VOWELS):
        #this is the case where the word begins with a vowel, and so we return [word] + "yay"
        return word + "yay"
    else:
        #this is the case where the word
        firstVowel = min([i if word[i] in VOWELS else INF for i in range(len(word))])
        wordStart = word[0:firstVowel]