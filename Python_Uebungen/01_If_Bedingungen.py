import random
x = random.randint(0,100)

print(x)

if(x < 20):
    print("Mini")
elif(x >= 20 and x <= 50):
    print("Medium")
else:
    print("Large")