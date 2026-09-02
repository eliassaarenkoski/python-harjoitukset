#Muokkaa peliprojektiohjelmaa niin, että jos käyttäjä syöttää iän, joka on alle 12 v., ohjelma ilmoittaa alaikäisyydestä ja sammuu. 
# Muussa tapauksessa ohjelma tervehtii käyttäjää, tulostaa päävalikon ja kysyy komentoja, kunnes käyttäjä kirjoittaa “lopeta”.
import random
nimi = input("Arvoisa pelaaja! Luo käyttäjä: ")
ika = int(input("Mikä on ikäsi?: "))
luku1 = int(random.randint(2,10))
luku2 = int(random.randint(2,10))
luku3 = int(random.randint(5,15))
luku4 = int(random.randint(3,4))
ytheensa1 = luku1 * luku2
ytheensa2 = luku3 / luku4

if ika < 12:
    print("Et ole tarpeeksi vanha tälle pelille")
elif ika >= 12:
    komento = 0
    while komento != "3":
        print("\nTervetuloa päävalikkoon!")
        print("1. Aloita lasku osa yksi")
        print("2. Aloita lasku osa kaksi")
        print("3. Lopeta laskut")
        komento = input("Määritä päävalikon arvo luvuilla 1-3: ")
        luku1 = int(random.randint(2,10))
        luku2 = int(random.randint(2,10))
        luku3 = int(random.randint(5,15))
        luku4 = int(random.randint(3,4))
        if komento == "1":
            ytheensa1 = float(input(f"laske lausekkeen arvo {luku1} * {luku2} = : "))
            if ytheensa1 == luku1 * luku2:
                print("vastaus on oikein")
            else:
                print("vastaus on väärin")
        if komento == "2":
            ytheensa2 = float(input(f"laske lausekkeen arvo {luku3} / {luku4} = : "))
            if ytheensa2 == luku3 / luku4:
                print("vastaus on oikein")
            else:
                print("vastaus on väärin")
        elif komento == "3":
            print("Peli loppui!")
        
