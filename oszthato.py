import random

def feladat2():
    print("A lista elemei: ")
    szamok = []
    print("\t", end = " ")
    for i in range(50):
        szam: int = random.randint(0, 100)
        szamok.append(int(szam))
        if i < 49:
            print(f"{szamok[i]}" , end = ", ")
        else:
            print(f"{szamok[i]}" , end = " ")
    return szamok

def hettelOszthato(szamok):
    db: int = 0
    for i in range(0, len(szamok), 1):
        if szamok[i] % 7 == 0:
            db += 1
    return db