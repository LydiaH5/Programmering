kör = input("Översätt ceasarchiffer. Skriv k för att kryptera och d för att dekryptera.\n")
while kör == "d" or kör == "D" or kör == "k" or kör == "K":
    if kör == "k" or kör == "K":
        kryptera = input("Skriv en text att kryptera:\n") 
        svar = ""
        for bokstav in kryptera:
            tal = ord(bokstav)
            tal = tal + 1
            # gör nästa gång: z går tillbaka till a
            svar = svar + chr(tal)
        print(svar)
        kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
    else:
        dekryptera = input("Skriv en text att dekryptera:\n")
        svar2 = ""
        for bokstav2 in dekryptera:
            tal2 = ord(bokstav2)
            tal2 = tal2 - 1
            svar2 = svar2 + chr(tal2)
        print(svar2)
        kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
print("Ogiltigt. Starta om")
