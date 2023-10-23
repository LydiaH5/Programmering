spela = input("Låt oss spela sten, sax, påse! Skriv vad du väljer.\n")
while spela == "sten" or spela == "sax" or spela == "påse":
    import random
    dator = (random.randrange(3))
    if dator == 0:
        print("Jag tog sten.")
        if spela == "sten":
            print("Det blev oavgjort!")
        elif spela == "sax":
            print("Jag vann!")
        elif spela == "påse":
            print("Du vann!")
    if dator == 1:
        print("Jag tog påse.")
        if spela == "sten":
            print("Jag vann!")
        elif spela == "sax":
            print("Du vann!")
        elif spela == "påse":
            print("Det blev oavgjort!")
    if dator == 2:
        print("Jag tog sax.")
        if spela == "sten":
            print("Du vann!")
        elif spela == "sax":
            print("Det blev oavgjort!")
        elif spela == "påse":
            print("Jag vann!")
    spela = input("Spela igen? Skriv sten, sax eller påse.\n")
print("Ogiltigt! Skriv sten, sax eller påse.")
    
