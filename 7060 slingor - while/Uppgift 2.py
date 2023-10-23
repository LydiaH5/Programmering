heltal = int(input("Hur många heltal vill du ha?\n"))
räknare = int(input("Vilket tal kommer först i serien?\n"))
maxtal = int(räknare + heltal)
while räknare < maxtal:
    print(räknare)
    räknare = räknare + 1
print("klar")
