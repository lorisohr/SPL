import random

Beenden = False

while Beenden == False:
    SpielStarten = input("1. Spiel starten\n2. Spiel beenden\nEingabe: ")

    if(SpielStarten == "1"):
        PlayerScore = 0
        CompScore = 0

        for i in range(0,6):
            PlayerWuerfel = random.randint(1,6)
            CompWuerfel = random.randint(1,6)

            input("Beliebigen Knopf zum würfeln drücken: ")

            print("\nSie haben eine " + str(PlayerWuerfel) + " gewürfelt")
            PlayerScore += PlayerWuerfel

            print("Der Computer hat eine " + str(CompWuerfel) + " gewürfelt\n")
            CompScore += CompWuerfel

            print("Spielstand:\nSpieler: " + str(PlayerScore) + "\tComputer:" + str(CompScore))

        print("Endstand:\nSpieler: " + str(PlayerScore) + "\tComputer: " + str(CompScore) + "\n")

        if CompScore == PlayerScore:
            print("Es ist ein unentschieden")

        elif CompScore > PlayerScore:
            print("Der Computer hat gewonnen")

        else:
            print("Sie haben gewonnen")
            
    else:
        Beenden = True




