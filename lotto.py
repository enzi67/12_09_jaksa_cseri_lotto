import random

def lotto_game():
    print("Üdvözlünk a lottó játékban!")
    
    jatekos_szamok = list(str(input("Adj meg 5 számot 1 és 90 között, vesszővel elválasztva: ")))

    nyero_szamok = random.sample(range(1, 91), 5)
    
    korok = len(set(jatekos_szamok) & set(nyero_szamok))
    
    print(f"A te számaid: {jatekos_szamok}")
    print(f"A nyerőszámok: {nyero_szamok}")
    print(f"Találatok száma: {korok}")

lotto_game()
