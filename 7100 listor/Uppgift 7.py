import random
kortlek = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
spela = input("Black Jack - Kom så nära 21 du kan utan att komma över. Skriv s för att spela.\n")
while spela == "s":
    summa = 0
    kort = []
    kort.append(random.randint(1, 13))
    kort.append(random.randint(1, 13))
    summa = summa + kort[0] + kort[1]
    print("Kort 1:", kort[0], "Kort 2:", kort[1])
    print("Totalt:", summa)
    if summa <= 21:
        drag = input("Välj h för hit och s för stand.\n")
        while drag == "h":
            kort.append(random.randint(1, 13))
            summa = summa + kort[-1]
            print("Kort:", kort[-1])
            print("Totalt:", summa)
            if summa >= 21:
                print("Du förlorade!")
                spela = input("Skriv s för att spela igen.")
            drag = input("Välj h för hit och s för stand.\n")
        if drag == "s":
            dator = 0
            datorkort = []
            datorkort.append(random.randint(1, 13))
            datorkort.append(random.randint(1, 13))
            dator = dator + sum(datorkort)
            while dator <= 16:
                datorkort.append(random.randint(1, 13))
                dator = dator + sum(datorkort)
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
        else:
            print("Ogiltigt kommando.")
    else:
        print("Du förlorade!")
    spela = input("Skriv s för att spela igen.")
print("Ogiltigt kommando. Starta om")
