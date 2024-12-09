import random

def lottó_játék():
    print("Üdvözöllek a lottó játékban!")
    print("Választható lottó típusok:")
    print("1. Ötöslottó (5 szám, 1-90)")
    print("2. Hatoslottó (6 szám, 1-45)")
    print("3. Skandináv lottó (7 szám, 1-35)")
    
    választás = int(input("Válaszd ki a lottó típusát (1/2/3): "))
    
    if választás == 1:
        max_szám = 90
        tipp_szám = 5
    elif választás == 2:
        max_szám = 45
        tipp_szám = 6
    elif választás == 3:
        max_szám = 35
        tipp_szám = 7
    else:
        print("Érvénytelen választás (⊙ˍ⊙). Kilépés... 👋")
        return
    
    print(f"\nKérlek, add meg a {tipp_szám} tippedet (1-{max_szám} között):")
    tippek = []
    
    for i in range(tipp_szám):
        while True:
            try:
                tipp = int(input(f"{i + 1}. tipp: "))
                if tipp < 1 or tipp > max_szám:
                    print(f"A számnak 1 és {max_szám} között kell lennie!")
                elif tipp in tippek:
                    print("Ezt a számot már egyszer megadtad!")
                else:
                    tippek.append(tipp)
                    break
            except ValueError:
                print("Érvénytelen bemenet 😭, kérlek számot adj meg!")
    
    nyerőszámok = random.sample(range(1, max_szám + 1), tipp_szám)
    print(f"Nyerőszámok: {sorted(nyerőszámok)}")
    
    találatok = len(set(tippek) & set(nyerőszámok))
    print(f"A te tippjeid: {sorted(tippek)}")
    print(f"Találatok száma: {találatok} / {tipp_szám}")
    
    if találatok == tipp_szám:
        print("Szerencsés! Telitalálat! 👌")
    else:
        print("Köszönjük, hogy játszottál! Próbáld újra!")

lottó_játék()