from Auto import Auto

slista = []
fajlom = open("auto.txt", "r", encoding = "UTF-8")
fajlom.readline()
lista = fajlom.readlines()
fajlom.close()
for i in range(0, len(lista), 1):
    sor_lista = lista[i].strip()
    sor_lista = lista[i].split(":")
    nev = sor_lista[0]
    gyart = sor_lista[1]
    autok = Auto(nev, int(gyart))
    slista.append(autok)

for i in range(0, len(slista), 1):
    print(f"{slista[i].snev}, {slista[i].gyartdatum}")