import random 
print("start")
poäng = 0
p = []
for i in range(16):
    p.append(0)
giltigt = 1
runda = 0
kategorier = []
kategorier2 = [0, "Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor", "Par", "Tvåpar", "Tretal", "Fyrtal", "Kåk", "Liten stege", "Stor stege", "Chans", "Yatzy"]
spela = input("Yatzy! Skriv s för att påbörja spel.\n")
while spela == "s":
    runda = runda + 1
    delrunda = 0
    tärningar = []
    for i in range(5):
        tärningar.append(random.randint(1, 6))
    print("Dina första 5 tärningar blev:", tärningar)
    while delrunda < 2: 
        kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")    
        while kasta != 0: 
            kast = []
            for char in kasta:
                if char.isdigit():
                    kast.append(int(char))
            if sum(kast) == 0:
                kasta = input("Ogiltigt! Skriv minst en siffra.\n")
            elif 0 in kast:
                delrunda = 2
            else:
                for i in kast:
                    tärningar.pop(i-1)
                    tärningar.insert(i-1, random.randint(1, 6))
                print("Dina tärningar är nu", tärningar)
                delrunda = delrunda + 1
    tärningar.sort()
    result = []
    noresult = [0]
    for i in range(1, 7):
        if i not in tärningar or i in kategorier: 
            noresult.append(i) 
    for i in tärningar:
        n = tärningar.count(i)
        if n > 1:
            result.append(i)
    for i in range(6, 16):
        if i in kategorier:
            noresult.append(i)
    if len(result) > 0:
        if result[0] != result[1]:
            noresult.append(7)
    if len(result) > 2:
        if result[2] != result[3]:
            noresult.append(8)
        if result[0] != result[3]:
            noresult.append(10)
    if len(result) == 5:
        if result[0] != result[2] or result[2] != result[4]:
            noresult.append(9)
        if (result[0] != result[1] and result[2] != result[4] 
            or result[0] != result[2] and result[3] != result[4]):
                noresult.append(11)
    if 1 and 2 and 3 and 4 and 5 not in tärningar:
        noresult.append(12) 
    if 2 and 3 and 4 and 5 and 6 not in tärningar:
        noresult.append(13)
    if tärningar[0] != tärningar[4]:
        noresult.append(15)
    if sum(noresult) == 120:
        print("Ditt resultat passar  inte någonstans! Välj en kategori att stryka:\n\nEttor (1) (", p[1], "poäng)\nTvåor (2) (", p[2], "poäng)\nTreor (3) (", p[3], "poäng)\nFyror (4) (", p[4], "poäng)\nFemmor (5) (", p[5], "poäng)\nSexor (6) (", p[6], "poäng)\nEtt par (7) (", p[7], "poäng)\nTvå par (8) (", p[8], "poäng)\nTretal (9) (", p[9], "poäng)\nFyrtal (10) (", p[10], "poäng)\nLiten stege (11) (", p[11], "poäng)\nStor stege (12) (", p[12], "poäng)\nKåk (13) (", p[13], "poäng)\nChans (14) (", p[14], "poäng)")
        släng = int(input("Yatzy (15) (", p[15], "poäng)\n"))
        p[släng] = 0
        if släng not in kategorier:
            kategorier.append(släng)
        print("Runda", runda, "avslutad. Dina totala poäng:", poäng)
        spela = input("Skriv s för att påbörja nästa runda.")         
    placera = int(input("Välj en av följande kategorier att placera resultatet i:\n\n Ettor (1)\n Tvåor (2)\n Treor (3)\n Fyror (4)\n Femmor (5)\n Sexor (6)\n Ett par (7)\n Två par (8)\n Tretal (9)\n Fyrtal (10)\n Kåk (11)\n Liten stege (12)\n Stor stege (13)\n Chans (14)\n Yatzy (15)\n"))
    while placera != "0":
        if placera in kategorier:
            placera = int(input("Kategorin", kategorier2[placera], "är upptagen. Välj en annan kategori.\n"))
        elif placera in noresult:
            placera = int(input("Du har inga", kategorier2[placera], "att placera! Välj en annan kategori.\n"))
        else:
            if placera < 7:
                for i in tärningar:
                    if i == placera:
                        p[placera] = p[placera] + placera
            if placera == 7:
                p[7] = p[7] + result[-1] + result[-2]
            if placera == 8:
                if result[2] == result[3]:
                    p[8] = p[8] + result[0] + result[1] + result[2] + result[3]
                else:
                    p[8] = p[8] + result[0] + result[1] + result[3] + result[4]
            if placera == 9:
                if result[0] == result[2]:
                    p[9] = p[9] + result[0] + result[1] + result[2]
                else:
                    p[9] = p[9] + result[-1] + result[-2] + result[-3]
            if placera == 10:
                p[10] = p[10] + result[-1] + result[-2] + result[-3] + result[-4]
            if placera == 11 or placera == 14:
                p[placera] = p[placera] + sum(tärningar)
            if placera == 12:
                p[12] = p[12] + 15
            if placera == 13:
                p[13] = p[13] + 20
            if placera == 15:
             p[15] = p[15] + 50
            kategorier.append(placera) 
            poäng = poäng + p[placera]
        if p[1] + p[2] + p[3] + p[4] + p[5] + p[6] >= 63: 
            poäng = poäng + 50
            print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
        if sum(kategorier) == 120:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!") 
        else:
            print("Runda", runda, "avslutad. Du har nu", p[placera], "poäng i kategorin", kategorier2[placera], "och ditt totala resultat är", poäng, "poäng.")
            spela = input("Skriv s för att påbörja nästa runda.\n")
        placera = "0"
print("Ogiltigt! Starta om programmet.")