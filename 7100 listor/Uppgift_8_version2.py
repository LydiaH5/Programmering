import random 
print("start")
poäng = 0
p = []
for i in range(16):
    p.append(0)
runda = 0
kategorier = []
kategorier2 = [0, Ettor, Tvåor, Treor, Fyror, Femmor, Sexor, Par, Tvåpar, Tretal, Fyrtal, Kåk, Liten stege, Stor stege, Chans, Yatzy]
spela = input("Yatzy! Skriv s för att påbörja spel.\n")
while spela == "s":
    runda = runda + 1
    noresult = 0
    tärningar = []
    for i in range(5):
        tärningar.append(random.randint(1, 6))
    print("Dina första 5 tärningar blev:", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")    
    kast = []
    for char in kasta:
        if char.isdigit():
            kast.append(int(char))
    if 0 in kast:
        print("")
    else:
        for i in kast:
            tärningar.pop(i-1)
            tärningar.insert(i-1, random.randint(1, 6))
    print("Dina tärningar är nu", tärningar)
    kasta = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.\n")    
    kast = []
    for char in kasta:
        if char.isdigit():
            kast.append(int(char))
    if 0 in kast:
        print("")
    else:
        for i in kast:
            tärningar.pop(i-1)
            tärningar.insert(i-1, random.randint(1, 6))
    print("Dina tärningar är nu", tärningar)
    #testa vilka placera som går:

    if noresult == 1: #if inget resultat passar:
        print("Ditt resultat passar  inte någonstans! Välj en kategori att stryka:\n\nEttor (1) (", p[1], "poäng)\nTvåor (2) (", p[2], "poäng)\nTreor (3) (", p[3], "poäng)\nFyror (4) (", p[4], "poäng)\nFemmor (5) (", p[5], "poäng)\nSexor (6) (", p[6], "poäng)\nEtt par (7) (", p[7], "poäng)\nTvå par (8) (", p[8], "poäng)\nTretal (9) (", p[9], "poäng)\nFyrtal (10) (", p[10], "poäng)\nLiten stege (11) (", p[11], "poäng)\nStor stege (12) (", p[12], "poäng)\nKåk (13) (", p[13], "poäng)\nChans (14) (", p[14], "poäng)")
        släng = int(input("Yatzy (15) (", p[15], "poäng)\n"))
        p[släng] = 0
        if släng not in kategorier:
            kategorier.append(släng)
        print("Runda", runda, "avslutad. Dina totala poäng är", poäng)
        spela = input("Skriv s för att påbörja nästa runda.")           
    placera = int(input("Välj en av följande kategorier att placera resultatet i:\n\n Ettor (1)\n Tvåor (2)\n Treor (3)\n Fyror (4)\n Femmor (5)\n Sexor (6)\n Ett par (7)\n Två par (8)\n Tretal (9)\n Fyrtal (10)\n Kåk (11)\n Liten stege (12)\n Stor stege (13)\n Chans (14)\n Yatzy (15)\n"))
    while placera != 0:
        if placera in kategorier:
            placera = input("Kategorin", kategorier2[placera], "är upptagen. Välj en annan kategori.\n")
        if 1 == 1: #ändra till if placera ej är möjligt
            placera = input("Du har inga", kategorier2[placera], "att placera! Välj en annan kategori.\n")
        else:
        #ge poäng
            kategorier.append(placera) 
            poäng = poäng + p[placera]
        if p[1] + p[2] + p[3] + p[4] + p[5] + p[6] >= 63: 
            poäng = poäng + 50
            print("Dina poäng i övre halvan är nu över 63. 50 poäng bonus!")
        if sum(kategorier) == 120:
                print("Ditt protokoll är fyllt! Spelet är nu avslutat. Ditt resultat:", poäng, "poäng!") 
        else:
            print("Runda", runda, "avslutad. Du har nu", p[placera], "poäng i kategorin", kategorier2[placera] "och dina totala poäng är:", poäng)
            spela = input("Skriv s för att påbörja nästa runda.\n")