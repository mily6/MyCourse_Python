import random
import time
from time import sleep
class Wojownik:
    def __init__(self,imie="",pZycia=0,pAtaku=0,pObrony=0):
        self.imie=imie
        self.pZycia=pZycia
        self.pAtaku=pAtaku
        self.pObrony=pObrony

    def atak(self):
        return random.randint(40,self.pAtaku)

    def obrona(self):
        return random.randint(20,self.pObrony)

    def straconeZycie(self, ilosc):
        self.pZycia -= ilosc

    def czyZywy(self):
            if self.pZycia <= 0:
                return False
            else:
                return True
    def __str__(self):
        return self.imie

def walka(malpa,rycerz):
    i = 1
    while malpa.czyZywy() and rycerz.czyZywy():
        print("Runda:", i)
        if random.randint(0,1)==0:
            pojedynek(malpa,rycerz)
        else:
            pojedynek(rycerz,malpa)
        statystyki(malpa,rycerz)
        i+=1
        time.sleep(5)
    if rycerz.czyZywy():
        print("Rycerz wygral walke")
    else:
        print("")
        print("Malpa wygrala walke!")


def pojedynek(x,y):
    print(y,"zostal zaatakowany przez",x)
    obrazenia=x.atak()-y.obrona()
    print(y,"stracil",obrazenia,"punktow zycia.")
    y.straconeZycie(obrazenia)

def statystyki(x,y):
    for i in (x,y):
        print(i,"ma",i.pZycia,"punkty zycia.")

rycerz=Wojownik("Rycerz",random.randint(200,250),random.randint(50,70),random.randint(25,40))
malpa=Wojownik("Malpa",random.randint(200,250),random.randint(50,70),random.randint(25,40))
walka(malpa,rycerz)
