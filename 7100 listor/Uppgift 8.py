import random 
poäng = 0
spela = input("Yatzy! Skriv s för att påbörja spel.\n")
while spela == "s":
    tärningar = [] 
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    print("Dina första 5 tärningar blev:", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")
    for tärning in kasta:
        if "1" in kasta:
            tärningar.remove(tärningar[0])
            tärningar.insert(0, random.randint(1, 6))
        if "2" in kasta:
            tärningar.remove(tärningar[1])
            tärningar.insert(1, random.randint(1, 6))
        if "3" in kasta:
            tärningar.remove(tärningar[2])
            tärningar.insert(2, random.randint(1, 6))
        if "4" in kasta:
            tärningar.remove(tärningar[3])
            tärningar.insert(3, random.randint(1, 6))
        if "5" in kasta:
            tärningar.remove(tärningar[4])
            tärningar.insert(4, random.randint(1, 6))
        if "0" in kasta:
            print("")
    print("Dina tärningar är nu", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")
    for tärning in kasta:
        if "1" in kasta:
            tärningar.remove(tärningar[0])
            tärningar.insert(0, random.randint(1, 6))
        if "2" in kasta:
            tärningar.remove(tärningar[1])
            tärningar.insert(1, random.randint(1, 6))
        if "3" in kasta:
            tärningar.remove(tärningar[2])
            tärningar.insert(2, random.randint(1, 6))
        if "4" in kasta:
            tärningar.remove(tärningar[3])
            tärningar.insert(3, random.randint(1, 6))
        if "5" in kasta:
            tärningar.remove(tärningar[4])
            tärningar.insert(4, random.randint(1, 6))
        if "0" in kasta:
            print("")
    print("Dina tärningar är nu", tärningar)
    poäng = poäng + sum(tärningar)
    tärningar.sort()
    placera = input("Välj en av följande kategorier att placera resultatet i:\n Ettor (1)\n Tvåor (2)\n Treor (3)\n Fyror (4)\n Femmor (5)\n Sexor (6)\n Ett par (7)\n Två par (8)\n Tretal (9)\n Fyrtal (10)\n Liten stege (11)\n Stor stege (12)\n Kåk (13)\n Chans (14)\n Yatzy (15)\n")
    if placera == "1":
        if 1 not in tärningar:
            print("Du har inga ettor! Välj en annan kategori.\n")
        else:
            print("Runda", runda, "Avslutad. Resultat:")
    if poäng >= 63: 
        poäng = poäng + 50
        print("Resultatet blev mer än 63. 50 poäng bonus!")
    if tärningar[0] == tärningar[4]:
        poäng = poäng + 50
        print("Yatzy! 50 poäng bonus!") 