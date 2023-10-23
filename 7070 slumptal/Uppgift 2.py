belopp = 100
print("Välkommen att spela Lucky Seven! Ett spel kostar 5 kronor.\n Tre sjuor ger vinst och 50 kronor. Två lika tal ger minivinst och 5 kronor. En sjua ger sjuvinst och 2 kronor.\n")
spela = input("Skriv j för att spela och n för att avsluta.\n")
while spela != "n":
    if spela == "j":
        while belopp <= 4:
            input("Du har slut på pengar!")
        belopp = belopp - 5
        import random
        tal1 = random.randrange(1, 10)
        tal2 = random.randrange(1, 10)
        tal3 = random.randrange(1, 10)
        print(tal1, tal2, tal3)
        if tal1 == 7 and tal2 == 7 and tal3 == 7:
            belopp = belopp + 50
            print("Vinst! Du vann 50 kronor! Du har nu kvar", belopp, "kronor.")
        elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
            belopp = belopp + 5
            print("Minivinst! Du vann 5 kronor! Du har nu kvar", belopp, "kronor.")
        elif tal1 == 7 or tal2 == 7 or tal3 == 7:
            belopp = belopp + 2
            print("Sjuvinst! Du vann 2 kronor! Du har nu kvar", belopp, "kronor.")
        else:
            print("Ingen vinst. Du har nu kvar", belopp, "kronor.")
        spela = input("Spela igen? j för ja och n för nej.\n")
    else:
        print("Ogiltigt kommando.")
print ("Du har nu", belopp, "kronor. Välkommen åter!")
