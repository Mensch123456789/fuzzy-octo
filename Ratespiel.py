import random
import time

#Versuche = 0

def start():
    Zahl = random.randint(-1, 101)
    print("Errate eine Zahl von -1 - 101!")

    raten(Zahl, 1)
    
def raten(Zahl, Versuche):
    
    try:
        Rateversuch = int(input("Was ist deine Vermutung?"))
    except ValueError:
        print("Nur Zahleneingaben sind erlaubt!")
        raten(Zahl, Versuche)


    if Rateversuch == Zahl:
        print(f"Richtig! Du hast {Versuche} Versuche gebraucht.")

        
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

    
    else:
        if Rateversuch <= Zahl:
            print("Größer")
        elif Rateversuch >= Zahl:
            print("KLeiner")
        
        raten(Zahl, Versuche+1)

    
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
