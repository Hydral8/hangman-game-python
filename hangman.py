import urllib3
import random
http = urllib3.PoolManager()
word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

res = http.request('GET', word_site)
txt = res.data.decode()

WORDS = txt.splitlines()


def genRandomWord():
    word = WORDS[random.randint(0, len(WORDS) - 1)]
    return word


def guess(word, correctLetters, usedLetters):
    print("Guess a letter!")
    letter = input()
    while(letter in usedLetters):
        print("Already used that letter!")
        letter = input()

    # add new letter to used lettesr
    usedLetters.add(letter.lower())
    usedLetters.add(letter.capitalize())

    # if letter exists in word, add to correct letters
    if((letter in word or letter.capitalize() in word) and letter != ""):
        print("Correct Letter!")
        correctLetters.add(letter.capitalize())
        correctLetters.add(letter.lower())
        return True
    else:
        print("Letter Does Not Exist!")
        return False


def printCurrentLetters(word, correctLetters):
    string = ""
    for letter in word:
        letter = str(letter)
        if(letter in correctLetters):
            string += letter
        else:
            string += "_"
    print(string)


def playGame():
    word = str(genRandomWord())
    word = word.upper()
    length = len(word)
    print("_" * length)
    allNeededLetters = set(word)
    correctLetters = set()
    usedLetters = set()
    print(word)
    while(not allNeededLetters.issubset(correctLetters)):
        if(guess(word, correctLetters, usedLetters)):
            printCurrentLetters(word, correctLetters)


playGame()
