svar = int(input("Gissa vilket heltal jag tänker på!\n"))
while svar != 4:
    svar = int(input("Fel. Försök igen!\n"))
print("Du gissade rätt!")
svar = int(input("Nu får du gissa ett nytt heltal.\n"))
försök = 0
while svar != 42:
    if svar < 42:
        print("Det är för litet! Du har", 2 - försök, "försök kvar.")
        svar = int(input())
        försök = försök + 1
    if svar > 42:
        print("Det är för stort! Du har", 2 - försök, "försök kvar.")
        svar = int(input())
        försök = försök + 1
    if försök == 2:
        print("Du förlorade!")
if svar == 42:
        print("Du gissade rätt! Det tog", försök, "försök.\n")
