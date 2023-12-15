import random 
spela = input("Yatzy! Skriv s för att påbörja spel och p för att se protokollet.\n")
while spela != "p":
    tärningar = [] 
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    tärningar.append(random.randint(1, 6))
    print("Dina första 5 tärningar blev:", tärningar)
    spara = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.")
    for tärning in spara:
        if "1" in spara:
            tärningar.remove(tärningar[0])
            tärningar.insert(0, random.randint(1, 6))
        if "2" in spara:
            tärningar.remove(tärningar[1])
            tärningar.insert(1, random.randint(1, 6))
        if "3" in spara:
            tärningar.remove(tärningar[2])
            tärningar.insert(2, random.randint(1, 6))
        if "4" in spara:
            tärningar.remove(tärningar[3])
            tärningar.insert(3, random.randint(1, 6))
        if "5" in spara:
            tärningar.remove(tärningar[4])
            tärningar.insert(4, random.randint(1, 6))
        if "0" in spara:
            print("")
    print("Dina tärningar är nu", tärningar)
    spara = input("Välj tärningar från 1-5 att kasta eller 0 för att behålla alla.")
    for tärning in spara:
        if "1" in spara:
            tärningar.remove(tärningar[0])
            tärningar.insert(0, random.randint(1, 6))
        if "2" in spara:
            tärningar.remove(tärningar[1])
            tärningar.insert(1, random.randint(1, 6))
        if "3" in spara:
            tärningar.remove(tärningar[2])
            tärningar.insert(2, random.randint(1, 6))
        if "4" in spara:
            tärningar.remove(tärningar[3])
            tärningar.insert(3, random.randint(1, 6))
        if "5" in spara:
            tärningar.remove(tärningar[4])
            tärningar.insert(4, random.randint(1, 6))
        if "0" in spara:
            print("")
    print("Dina tärningar är nu", tärningar)
