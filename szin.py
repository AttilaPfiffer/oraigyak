import math
import random

def feladat1():
    print("Első feladat:")
    szin: str = str(input("\tKérek egy színkeverési módszert: "))
    szin_kod: str = str(input("\tKérem a kódot:"))
    if szin == "RGB":
        if len(szin_kod) >= 5 and len(szin_kod) <= 11:
            print("\tMegfelelő hossz")
        else:
            print("\tNem megfelelő hossz")
    if szin == "HSL":
        if len(szin_kod) >= 7 and len(szin_kod) <= 13:
            print("\tMegfelelő hossz")
        else:
            print("\tNem megfelelő hossz")
    if szin == "HEX":
        if len(szin_kod) == 6:
            print("\tMegfelelő hossz")
        else:
            print("\tNem megfelelő hossz")
    
