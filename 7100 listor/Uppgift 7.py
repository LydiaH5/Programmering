import random
spela = input("Black Jack - Kom så nära 21 du kan utan att komma över. Skriv s för att spela.\n")
while spela == "s":
    summa = 0
    kort = []
    kort.append(random.randint(1, 13))
    kort.append(random.randint(1, 13))
    summa = summa + sum(kort)
    print("Kort 1:", kort[0], "Kort 2:", kort[1])
    print("Totalt:", summa)
    if summa < 21:
        drag = input("Välj h för hit och s för stand.\n")
        while drag == "h":
            kort.append(random.randint(1, 13))
            summa = summa + kort[-1]
            print("Kort:", kort[-1])
            print("Totalt:", summa)
            if summa > 21:
                print("Du förlorade!")
                drag = "restart"
        if drag == "s":
            dator = 0
            datorkort = []
            datorkort.append(random.randint(1, 13))
            datorkort.append(random.randint(1, 13))
            dator = dator + sum(datorkort)
            while dator <= 16:
                datorkort.append(random.randint(1, 13))
                dator = dator + datorkort[-1]
            print("Datorn fick:", dator)
            if dator > 21:
                print("Du vann!")
            elif dator <= 21:
                if dator > sum(kort):
                    print("Datorn vann!")
                elif dator == sum(kort):
                    print("Lika!")
                elif dator < sum(kort):
                    print("Du vann!")
        elif drag != "restart":
            print("Ogiltigt kommando.")
    else:
        print("Du förlorade!")
    spela = input("Skriv s för att spela igen.\n")
print("Ogiltigt kommando. Starta om")
