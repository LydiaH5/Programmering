tal = int(input("Skriv ett tal.\n"))
if tal >= 0:
    print("talet är positivt.")
else:
    print("talet är negativt.")
siffra = int(input("Vad är näst sista siffran i ditt personnummer?\n"))
if siffra %2 == 0:
    print("du är en kvinna")
else:
    print("du är en man")
talett = int(input("Skriv nu två tal.\n"))
taltvå = int(input(""))
if talett > taltvå:
    print(talett, "är större än", taltvå)
elif talett == taltvå:
    print("Talen är lika stora!") 
else:
    print(taltvå, "är större än", talett)
nummer = int(input("Nu behövs ett nytt tal.\n"))
if nummer < 0:
    print("Detta är ett negativt tal.")
elif nummer >= 0 and nummer < 10:
    print("Detta är ett ensiffrigt tal.")
elif nummer >= 10 and nummer < 100:
    print("Detta är ett tvåsiffrigt tal.")
elif nummer >= 100 and nummer < 1000:
    print("Detta är ett tresiffrigt tal.")
else:
    print:("Detta är minst ett fyrsiffrigt tal.")
siffraett = int(input("Ge mig tre olika tal.\n"))
siffratvå = int(input(""))
siffratre = int(input(""))
if siffraett < siffratvå and siffratvå < siffratre:
    print(siffraett, "är minst! I storleksordning blir det", siffraett, siffratvå, siffratre)
elif siffraett < siffratre and siffratre < siffratvå:
    print(siffraett, "är minst! I storleksordning blir det", siffraett, siffratre, siffratvå)
elif siffratvå < siffraett and siffraett < siffratre:
    print(siffratvå, "är minst! I storleksordning blir det", siffratvå, siffraett, siffratre)
elif siffratvå < siffratre and siffratre < siffraett:
    print(siffratvå, "är minst! I storleksordning blir det", siffratvå, siffratre, siffraett)
elif siffratre < siffraett and siffraett < siffratvå:
    print(siffratre, "är minst! I storleksordning blir det", siffratre, siffraett, siffratvå)
elif siffratre < siffratvå and siffratvå < siffraett:
    print(siffratre, "är minst! I storleksordning blir det", siffratre, siffratvå, siffraett)
