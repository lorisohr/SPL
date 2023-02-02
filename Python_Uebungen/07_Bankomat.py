class Bankomat:
    def __init__(User, Kontostand):
        User.Kontostand = Kontostand

    def Einzahlen(User, Betrag):
        User.Kontostand += Betrag
        print("Sie haben " + str(Betrag) + "€ eingezahlt")
    
    def Auszahlen(User, Betrag):
        User.Kontostand -= Betrag
        print("Sie haben " + str(Betrag) + "€ abgehoben")

    def fKontostand(User):
        print("Ihr Kontostand beträgt: " + str(User.Kontostand) + "€")

Beenden = False

Person = Bankomat(0)

while Beenden == False:
    Input = input("1. Einzahlen\n2. Auszahlen\n3. Kontostand\n4. Ende\nAuswahl: ")
    if(Input == "1"):
        EinzahlBetrag = int(input("Wieviel wollen Sie einzahlen: "))
        Person.Einzahlen(EinzahlBetrag)
    elif(Input == "2"):
        AuszahlBetrag = int(input("Wieviel wollen Sie abheben: "))
        if Person.Kontostand < AuszahlBetrag:
            print("Sie haben nicht genug geld auf dem Konto!")
        else:
            Person.Auszahlen(AuszahlBetrag)
    elif(Input == "3"):
        Person.fKontostand()
    elif(Input == "4"):
        Beenden = True
    else:
        print("Keine gültige Auswahl!")
