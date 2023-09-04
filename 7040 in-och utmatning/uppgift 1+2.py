färg = input("Vad är din favoritfärg?\n")
namn = input("Vad heter du då?\n")
print("Hej", namn, sep=", ", end="! "),print(färg, "är min favoritfärg också!")
bas = float(input("Ge mig nu basen för en triangel.\n"))
höjd = float(input("Och nu höjden?\n"))
area = bas * höjd / 2
print("Perfekt! Din bas är", bas, "och din höjd är", höjd, end=". "),print("Din area blir då", area, end="!\n")
radie = float(input("Nu söker jag radien för en cirkel. \n"))
area2 = radie**2 * 3.14
omkrets = 2 * radie * 3.14
print("Då får du arean", area, "och omkretsen", omkrets, end=". Visst är matte kul?") 
