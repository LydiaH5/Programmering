Ord = input("Skriv en text för att översätta till rövarspråk.\n")
svar = ""
vokaler = "aeiuoyåäö "
for bokstav in Ord:
    if bokstav not in vokaler:
        svar += bokstav + "o" + bokstav
    elif bokstav == " ":
        svar = svar + " "
    else:
        svar = svar + bokstav
print(svar)
