import random 
poäng = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0
p11 = 0
p12 = 0
p13 = 0
p14 = 0
p15 = 0
runda = 0
kategorier = []
spela = input("Yatzy! Skriv s för att påbörja spel.\n")
while spela == "s":
    runda = runda + 1
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
    while placera == "1":
        if "1" not in tärningar:
            placera = input("Du har inga ettor! Välj en annan kategori.\n")
        elif "1" in kategorier:
            placera = input("Kategorin Ettor är upptagen. Välj en annan kategori.\n")
        else:
            kategorier.append("1")
            kategorier.sort()
            for tärning in tärningar:
               if "1" in tärningar: 
                p1 = p1 + 1  
            poäng = poäng + p1
            if runda == 15:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!") 
            else:
                print("Runda", runda, "avslutad. Du har nu", p1, "poäng i kategorin Ettor. Dina totala poäng är", poäng)
                spela = input("Skriv s för att påbörja nästa runda.")
    while placera == "2":
        if "2" not in tärningar:
            placera = input("Du har inga tvåor! Välj en annan kategori.\n")
        elif "2" in kategorier:
            placera = input("Kategorin Tvåor är upptagen. Välj en annan kategori.\n")
        else:
            kategorier.append("2")
            kategorier.sort()
            for tärning in tärningar:
               if "2" in tärningar: 
                p2 = p2 + 2  
            poäng = poäng + p2
            if runda == 15:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
            else:
                print("Runda", runda, "avslutad. Du har nu", p2, "poäng i kategorin Tvåor. Dina totala poäng är", poäng)
                spela = input("Skriv s för att påbörja nästa runda.")   
    while placera == "3":
        if "3" not in tärningar:
            placera = input("Du har inga treor! Välj en annan kategori.\n")
        elif "3" in kategorier:
            placera = input("Kategorin Treor är upptagen. Välj en annan kategori.\n")
        else:
            kategorier.append("3")
            kategorier.sort()
            for tärning in tärningar:
               if "3" in tärningar: 
                temppoäng = p3 + 3  
            poäng = poäng + p3
            if runda == 15:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
            else:
                print("Runda", runda, "avslutad. Du har nu", p3, "poäng i kategorin Treor. Dina totala poäng är", poäng)
                spela = input("Skriv s för att påbörja nästa runda.")
    while placera == "4":
        if "4" not in tärningar:
            placera = input("Du har inga fyror! Välj en annan kategori.\n")
        elif "4" in kategorier:
            placera = input("Kategorin Fyror är upptagen. Välj en annan kategori.\n")
        else:
            kategorier.append("4")
            kategorier.sort()
            for tärning in tärningar:
               if "4" in tärningar: 
                p4 = p4 + 4  
            poäng = poäng + p4
            if runda == 15:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
            else:
                print("Runda", runda, "avslutad. Du har nu", temppoäng, "poäng i kategorin Tvåor. Dina totala poäng är", poäng)
                spela = input("Skriv s för att påbörja nästa runda.")         
    while placera == "15":
        if tärningar[0] == tärningar[4]:
            poäng = poäng + 50
            print("Yatzy! 50 poäng bonus!")
        else:
            print("Runda", runda, "avslutad. Resultat:") 
    if poäng >= 63: 
        poäng = poäng + 50
        print("Resultatet blev mer än 63. 50 poäng bonus!")
