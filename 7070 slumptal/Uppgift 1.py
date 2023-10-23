svar = input("Vill du slå två tärningar? Två lika ger vinst. Skriv j eller n.\n")
while svar == "j":
    import random
    tal1 = random.randrange(1, 7)
    tal2 = random.randrange(1, 7)
    print(tal1, tal2)
    if tal1 == tal2:
        svar = input("Du vann! Vill du spela igen?\n")
    else:
        svar = input("Du förlorade. Vill du spela igen?\n")
if svar == "n":
    print("Välkommen åter!")
else:
    print("Det där var inget j eller n!") 
