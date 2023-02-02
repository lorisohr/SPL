import random

Boolean = True
RandomNumber = 0
Number = 0

while Boolean == True:
    RandomNumber = random.randint(10,30)
    print(RandomNumber)
    if(RandomNumber == 15 or RandomNumber == 25):
        Boolean = False     
    else:
        Number += RandomNumber

print(Number)