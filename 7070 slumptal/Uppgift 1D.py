belopp = 0
total = 0
print("Välkommen att kasta tärning! Ett spel kostar 2 kronor.\n Vinstplan:\n Två lika tärningar - 5 kr\n Sexa - 3 kr\n Stege - 3 kr\n")
händelse = input("Välj spela (s), sätt in pengar (i) eller avsluta (a).\n")
while händelse != "a":
    if händelse == "s":
        if belopp <= 0:
            print("Du har inte råd att spela! Sätt in pengar först.")
        else:
            belopp = belopp - 2
            import random
            tal1 = random.randrange(1, 7)
            tal2 = random.randrange(1, 7)
            print("Tärning 1:", tal1, "Tärning 2:", tal2)
            if tal1 == tal2:
                belopp = belopp + 5
                print("Två lika tärningar! Du vann 5 kronor. Ditt belopp är nu", belopp, "kronor.")
            elif tal1 == 6 or tal2 == 6:
                belopp = belopp + 3
                print("En sexa! Du vann 3 kronor. Ditt belopp är nu", belopp, "kronor.")
            elif tal1 == tal2 + 1 or tal2 == tal1 + 1:
                belopp = belopp + 3
                print("En stege! Du vann 3 kronor. Ditt belopp är nu", belopp, "kronor.")
            elif tal1 == 6 and tal2 == 6:
                belopp = belopp + 8
                print("Stjärnvinst! Du vann 8 kronor. Ditt belopp är nu", belopp, "kronor.")
            else:
                print("Du vann inte. Ditt belopp är nu", belopp, "kronor.")
    elif händelse == "i":
        sättin = int(input("Välj ett belopp att sätta in:\n"))
        belopp = belopp + sättin
        total = total + sättin
        print("Du har satt in", sättin, "kronor. Du har nu", belopp, "kronor att spela med.")
    else:
        print("Ogiltigt kommando!")
    händelse = input("Välj spela (s), sätt in pengar (i) eller avsluta (a).\n")
print("Totalt vann du", belopp - total, "kronor. Välkommen åter!") 
