kör = input("Översätt ceasarchiffer. Skriv k för att kryptera och d för att dekryptera.\n")
while kör == "d" or kör == "k":
    if kör == "k":
        antal = input("Välj antal steg att skifta: 1, 2 eller 3.\n")
        if antal == "1":
            kryptera = input("Skriv en text att kryptera:\n") 
            svar = ""
            for bokstav in kryptera:
                tal = ord(bokstav)
                if tal == 122:
                    tal = 229
                    svar = svar + chr(tal)
                elif tal == 229:
                    tal = 228
                    svar = svar + chr(tal)
                elif tal == 228:
                    tal = 246
                    svar = svar + chr(tal)
                elif tal == 246:
                    tal = 97
                    svar = svar + chr(tal)
                elif tal == 32:
                    tal = 32
                    svar = svar + chr(tal)
                else:
                    tal = tal + 1
                    svar = svar + chr(tal)
            print(svar)
            kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
        elif antal == "2":
            kryptera = input("Skriv en text att kryptera:\n") 
            svar = ""
            for bokstav in kryptera:
                tal = ord(bokstav)
                if tal == 121:
                    tal = 229
                    svar = svar + chr(tal)
                elif tal == 122:
                    tal = 228
                    svar = svar + chr(tal)
                elif tal == 229:
                    tal = 246
                    svar = svar + chr(tal)
                elif tal == 228:
                    tal = 97
                    svar = svar + chr(tal)
                elif tal == 246:
                    tal = 98
                    svar = svar + chr(tal)
                elif tal == 32:
                    tal = 32
                    svar = svar + chr(tal)
                else:
                    tal = tal + 2
                    svar = svar + chr(tal)
            print(svar)
            kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
        elif antal == "3":
            kryptera = input("Skriv en text att kryptera:\n") 
            svar = ""
            for bokstav in kryptera:
                tal = ord(bokstav)
                if tal == 120:
                    tal == 229 
                    svar = svar + chr(tal)
                elif tal == 121:
                    tal == 228 
                    svar = svar + chr(tal)
                elif tal == 122:
                    tal = 246
                    svar = svar + chr(tal)
                elif tal == 229:
                    tal = 97
                    svar = svar + chr(tal)
                elif tal == 228:
                    tal = 98
                    svar = svar + chr(tal)
                elif tal == 246:
                    tal = 99
                    svar = svar + chr(tal)
                elif tal == 32:
                    tal = 32
                    svar = svar + chr(tal)
                else:
                    tal = tal + 3
                    svar = svar + chr(tal)
            print(svar)
            kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
        else:
            kör = input("Ogiltigt. Skriv k för att kryptera och d för att dekryptera.\n")
    else:
        dekryptera = input("Skriv en text att dekryptera:\n")
        svar2 = ""
        svar3 = ""
        svar4 = ""
        for bokstav2 in dekryptera:
            tal2 = ord(bokstav2)
            if tal2 == 229:
                tal2 = 122
                svar2 = svar2 + chr(tal2)
            elif tal2 == 228:
                tal2 = 229
                svar2 = svar2 + chr(tal2) 
            elif tal2 == 246:
                tal2 = 228
                svar2 = svar2 + chr(tal2)
            elif tal2 == 97:
                tal2 = 246
                svar2 = svar2 + chr(tal2)
            elif tal2 == 32:
                tal2 = 32
                svar2 = svar2 + chr(tal2)
            else:
                tal2 = tal2 - 1
                svar2 = svar2 + chr(tal2)
        for bokstav3 in dekryptera:
            tal3 = ord(bokstav3)
            if tal3 == 229:
                tal3 = 121
                svar3 = svar3 + chr(tal3)
            elif tal3 == 228:
                tal3 = 122
                svar3 = svar3 + chr(tal3) 
            elif tal3 == 246:
                tal3 = 229
                svar3 = svar3 + chr(tal3)
            elif tal3 == 97:
                tal3 = 228
                svar3 = svar3 + chr(tal3)
            elif tal3 == 98: 
                tal3 = 246
                svar3 = svar3 + chr(tal3)
            elif tal3 == 32:
                tal3 = 32
                svar3 = svar3 + chr(tal3)
            else:
                tal3 = tal3 - 2
                svar3 = svar3 + chr(tal3)
        for bokstav4 in dekryptera:
            tal4 = ord(bokstav4)
            if tal4 == 229:
                tal4 = 120
                svar4 = svar4 + chr(tal4)
            elif tal4 == 228:
                tal4 = 121
                svar4 = svar4 + chr(tal4) 
            elif tal4 == 246:
                tal4 = 220
                svar4 = svar4 + chr(tal4)
            elif tal4 == 97:
                tal4 = 229
                svar4 = svar4 + chr(tal4)
            elif tal4 == 98: 
                tal4 = 228
                svar4 = svar4 + chr(tal4)
            elif tal4 == 99:
                tal4 = 246
                svar4 = svar4 + chr(tal4)
            elif tal4 == 32:
                tal4 = 32
                svar4 = svar4 + chr(tal4)
            else:
                tal4 = tal4 - 3
                svar4 = svar4 + chr(tal4)
        print("Ett steg:", svar2, "\n Två steg:", svar3, "\n Tre steg:", svar4)
        kör = input("Skriv k för att kryptera och d för att dekryptera.\n")
print("Ogiltigt. Starta om")
