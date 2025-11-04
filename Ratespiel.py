import random
import time

#Versuche = 0

def start():
    try:
        Spanne_min = int(input("Errate eine Zahl von ..."))
    except ValueError:
        print("Nur Zahleneingaben sind erlaubt!")
        start()
    try:
        Spanne_max = int(input("bis ..."))
    except ValueError:
        print("Nur Zahleneingaben sind erlaubt!")
        start()
    
    Zahl = random.randint(Spanne_min, Spanne_max)
    print(f"OK! Errate eine Zahl von {Spanne_min} bis {Spanne_max}!")

    raten(Zahl, 1, Spanne_min, Spanne_max)
    
def raten(Zahl, Versuche, min, max):
    
    Rateversuch_string = input("Was ist deine Vermutung? Tipp: Mit ? wird der geforderte Bereich angezeigt.")

    if Rateversuch_string == "?":
        print(f"Die gesuchte Zahl ist zwischen {min} und {max} (exklusive {min} und {max}).")
        raten(Zahl, Versuche, min, max)
    
    try:
        Rateversuch = int(Rateversuch_string)
    except ValueError:
        print("Nur Zahleneingaben sind erlaubt!")
        raten(Zahl, Versuche, min, max)

    min, max, in_gefordertem_Bereich =  gefordeter_Bereich(min, max, Zahl, Rateversuch)

    if in_gefordertem_Bereich:
        if Rateversuch == Zahl:
            print(f"Richtig! Du hast {Versuche} Versuche gebraucht.")
            Nochmal_Spielen()
        else:
            if Rateversuch <= Zahl:
                print("Größer")
            elif Rateversuch >= Zahl:
                print("KLeiner")
        
    raten(Zahl, Versuche+1, min, max)

def gefordeter_Bereich(min, max, Zahl, Rateversuch):
    in_gefordertem_Bereich = True
    if Rateversuch <= max and Rateversuch >= Zahl:
        max = Rateversuch
    elif Rateversuch >= min and Rateversuch <= Zahl:
        min = Rateversuch
    else:
        print(f"Die Zahl ist nicht im geforderten Bereich versuche es doch mit einer Zahl im Bereich von {min} - {max} (exklusive {min} und {max}).")
        in_gefordertem_Bereich = False
    return min, max, in_gefordertem_Bereich

def Nochmal_Spielen():
    erneut = input("Möchtest du erneut spielen? (ja/nein)")
    if erneut == "nein":
        print("ok")
        time.sleep(2)
        exit()
    elif erneut == "ja":
        print("Das Spiel startet nun neu")
        start()
    else:
        print("Bitte nur ja oder nein")
        Nochmal_Spielen()

start()
