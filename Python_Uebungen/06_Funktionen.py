def AddNumbers(x, y):
    print(x + y)

AddNumbers(2,3)

import random
def RandNumb():
    print(random.randint(100,200))

RandNumb()

def StringArrToWord(word):
    result = ""   
    for letter in range(0, len(word)): 
        result = result + word[letter]
    print(result)

Word = ["h", "e", "l", "l", "o"]
StringArrToWord(Word)
