import random 
print("start")
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
    noresult = 0
    tärningar = [] 
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    print("Dina första 5 tärningar blev:", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")    
    if "1" in kasta:
        tärningar.pop(0)
        tärningar.insert(0, random.randint(1, 6))
    if "2" in kasta:
        tärningar.pop(1)
        tärningar.insert(1, random.randint(1, 6))
    if "3" in kasta:
        tärningar.pop(2)
        tärningar.insert(2, random.randint(1, 6))
    if "4" in kasta:
        tärningar.pop(3)
        tärningar.insert(3, random.randint(1, 6))
    if "5" in kasta:
        tärningar.pop(4)
        tärningar.insert(4, random.randint(1, 6))
    if "0" in kasta:
        print("")
    print("Dina tärningar är nu", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")
    if "1" in kasta:
        tärningar.pop(0)
        tärningar.insert(0, random.randint(1, 6))
    if "2" in kasta:
        tärningar.pop(1)
        tärningar.insert(1, random.randint(1, 6))
    if "3" in kasta:
        tärningar.pop(2)
        tärningar.insert(2, random.randint(1, 6))
    if "4" in kasta:
        tärningar.pop(3)
        tärningar.insert(3, random.randint(1, 6))
    if "5" in kasta:
        tärningar.pop(4)
        tärningar.insert(4, random.randint(1, 6))
    if "0" in kasta:
        print("")
    print("Dina tärningar är nu", tärningar)
    tärningar.sort()
    #if inget resultat passar:
            #roresult = 1 
    if noresult == 1:
        print("Ditt resultat passar  inte någonstans! Välj en kategori att stryka:\n\nEttor (1) (", p1, "poäng)\nTvåor (2) (", p2, "poäng)\nTreor (3) (", p3, "poäng)\nFyror (4) (", p4, "poäng)\nFemmor (5) (", p5, "poäng)\nSexor (6) (", p6, "poäng)\nEtt par (7) (", p7, "poäng)\nTvå par (8) (", p8, "poäng)\nTretal (9) (", p9, "poäng)\nFyrtal (10) (", p10, "poäng)\nLiten stege (11) (", p11, "poäng)\nStor stege (12) (", p12, "poäng)\nKåk (13) (", p13, "poäng)\nChans (14) (", p14, "poäng)")
        släng = input("Yatzy (15) (", p15, "poäng)\n")
        if släng == "1":
            p1 = 0
            if 1 not in kategorier:
                kategorier.append(1) 
                kategorier.sort()
        elif släng == "2":
            p2 = 0
            if 2 not in kategorier:
                kategorier.append(2)
                kategorier.sort()
        elif släng == "3":
            p3 = 0
            if 3 not in kategorier:
                kategorier.append(3)
                kategorier.sort()
        elif släng == "4":
            p4 = 0
            if 4 not in kategorier:
                kategorier.append(4)
                kategorier.sort
        elif släng == "5":
            p5 = 0
            if 5 not in kategorier:
                kategorier.append(5)
                kategorier.sort()
        elif släng == "6":
            p6 = 0
            if 6 not in kategorier:
                kategorier.append(6)
                kategorier.sort()
        elif släng == "7":
            p7 = 0
            if 7 not in kategorier:
                kategorier.append(7)
                kategorier.sort()
        elif släng == "8":
            p8 = 0
            if 8 not in kategorier:
                kategorier.append(8)
                kategorier.sort
        elif släng == "9":
            p9 = 0
            if 9 not in kategorier:
                kategorier.append(9)
                kategorier.sort
        elif släng == "10":
            p10 = 0
            if 10 not in kategorier:
                kategorier.append(10)
                kategorier.sort
        elif släng == "11":
            p11 = 0
            if 11 not in kategorier:
                kategorier.append(11)
                kategorier.sort
        elif släng == "12":
            p12 = 0
            if 12 not in kategorier:
                kategorier.append(12)
                kategorier.sort
        elif släng == "13":
            p13 = 0
            if 13 not in kategorier:
                kategorier.append(13)
                kategorier.sort
        elif släng == "14":
            p14 = 0
            if 14 not in kategorier:
                kategorier.append(14)
                kategorier.sort
        elif släng == "15":
            p15 = 0
            if 15 not in kategorier:
                kategorier.append(15)
                kategorier.sort
        print("Runda", runda, "avslutad. Dina totala poäng är", poäng)
        spela = input("Skriv s för att påbörja nästa runda.")                    
    placera = input("Välj en av följande kategorier att placera resultatet i:\n\n Ettor (1)\n Tvåor (2)\n Treor (3)\n Fyror (4)\n Femmor (5)\n Sexor (6)\n Ett par (7)\n Två par (8)\n Tretal (9)\n Fyrtal (10)\n Liten stege (11)\n Stor stege (12)\n Kåk (13)\n Chans (14)\n Yatzy (15)\n")
    while placera != 0:
        while placera == "1":
            if 1 not in tärningar:
                placera = input("Du har inga ettor! Välj en annan kategori.\n")
            elif 1 in kategorier:
                placera = input("Kategorin Ettor är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(1)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 1: 
                        p1 = p1 + 1  
                poäng = poäng + p1
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!") 
                else:
                    print("Runda", runda, "avslutad. Du har nu", p1, "poäng i kategorin Ettor. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")
        while placera == "2":
            if 2 not in tärningar:
                placera = input("Du har inga tvåor! Välj en annan kategori.\n")
            elif 2 in kategorier:
                placera = input("Kategorin Tvåor är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(2)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 2: 
                        p2 = p2 + 2  
                poäng = poäng + p2
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    input("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
                else:
                    print("Runda", runda, "avslutad. Du har nu", p2, "poäng i kategorin Tvåor. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")   
        while placera == "3":
            if 3 not in tärningar:
                placera = input("Du har inga treor! Välj en annan kategori.\n")
            elif 3 in kategorier:
                placera = input("Kategorin Treor är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(3)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 3: 
                        p3 = p3 + 3  
                poäng = poäng + p3
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    input("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
                else:
                    print("Runda", runda, "avslutad. Du har nu", p3, "poäng i kategorin Treor. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")
        while placera == "4":
            if 4 not in tärningar:
                placera = input("Du har inga fyror! Välj en annan kategori.\n")
            elif 4 in kategorier:
                placera = input("Kategorin Fyror är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(4)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 4: 
                        p4 = p4 + 4  
                poäng = poäng + p4
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    input("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
                else:
                    print("Runda", runda, "avslutad. Du har nu", p4, "poäng i kategorin Fyror. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")
        while placera == "5":
            if 5 not in tärningar:
                placera = input("Du har inga femmor! Välj en annan kategori.\n")
            elif 5 in kategorier:
                placera = input("Kategorin Femmor är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(5)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 5:
                        p5 = p5 + 5  
                poäng = poäng + p5
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    input("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
                else:
                    print("Runda", runda, "avslutad. Du har nu", p5, "poäng i kategorin Femmor. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")
        while placera == "6":
            if 6 not in tärningar:
                placera = input("Du har inga sexor! Välj en annan kategori.\n")
            elif 6 in kategorier:
                placera = input("Kategorin Sexor är upptagen. Välj en annan kategori.\n")
            else:
                placera = 0
                kategorier.append(6)
                kategorier.sort()
                for tärning in tärningar:
                    if tärning == 6: 
                        p6 = p6 + 6  
                poäng = poäng + p6
                if p1 + p2 + p3 + p4 + p5 + p6 >= 63: 
                    poäng = poäng + 50
                    print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
                if sum(kategorier) == 120:
                    input("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!")
                else:
                    print("Runda", runda, "avslutad. Du har nu", p6, "poäng i kategorin Sexor. Dina totala poäng:", poäng)
                    spela = input("Skriv s för att påbörja nästa runda.\n")         
        while placera == "15":
            if tärningar[0] == tärningar[4]:
                poäng = poäng + 50
                print("Runda", runda, "avslutad. Resultat:") 
        if placera != 0:
            placera = input("Ogiltigt. Skriv en siffra 1-15.")

