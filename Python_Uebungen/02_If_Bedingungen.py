import random

x = random.randint(0, 100)
y = random.randint(0, 100)

if x < y and x < 50:
  print("Zahl 1 ist kleiner als Zahl2 und Mini")

if x < 30 or y < 30:
  print("Eine der beiden Zahlen ist kleiner als 30")

if x < 50 and y != 50:
  print("Erste Zahl klein, zweite kein 50iger")

print(x, y)