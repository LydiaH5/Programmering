kast = []
input("Skriv något för att kasta 10 tärningar.\n")
import random
for i in range(10):
    kast.append(random.randint(1,6))
print("Resultat:", kast)
kast.sort()
print("Sorterat:", kast)
print("Medelvärde:", sum(kast) / len(kast))
print("Minsta tal:", min(kast))
print("Största tal:", max(kast))
antal_sexor = 0
for sexa in kast:
    if sexa == 6:
        antal_sexor = antal_sexor + 1
print("Antal sexor:", antal_sexor)
antal_ettor = 0
for etta in kast:
    if etta == 1:
        antal_ettor = antal_ettor + 1
antal_tvåor = 0
for tvåa in kast:
    if tvåa == 2:
        antal_tvåor = antal_tvåor + 1
antal_treor = 0
for trea in kast:
    if trea == 3:
        antal_treor = antal_treor + 1
antal_fyror = 0
for fyra in kast:
    if fyra == 4:
        antal_fyror = antal_fyror + 1
antal_femmor = 0
for femma in kast:
    if femma == 5:
        antal_femmor = antal_femmor + 1
vanligast = [antal_ettor, antal_tvåor, antal_treor, antal_fyror, antal_femmor, antal_sexor]
vanligast.sort()
if vanligast[5] == antal_ettor: 
    print("Vanligaste valör: 1")
elif vanligast[5] == antal_tvåor:
    print("Vanligaste valör: 2")
elif vanligast[5] == antal_treor:
    print("Vanligaste valör: 3")
elif vanligast[5] == antal_fyror:
    print("Vanligaste valör: 4")
elif vanligast[5] == antal_femmor:
    print("Vanligaste valör: 5")
elif vanligast[5] == antal_sexor:
    print("Vanligaste valör: 6")
