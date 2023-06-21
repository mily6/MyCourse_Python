import random
from time import sleep

class Wojownik():
    def __init__(self,imie='anonim',zycie=0,pAtaku=0,pObrony=0):
        self.imie = imie
        self.zycie = zycie
        self.pAtaku = pAtaku
        self.pObrony = pObrony

    def atak(self):
        return random.randint(50,self.pAtaku)
    def obrona(self):
        return random.randint(10,self.pObrony)
    def straconeZycie(self,ilosc):
        self.zycie -= ilosc

    def czyZywy(self):
        if self.zycie <= 0:
            self.zycie = 0
            return False
        else:
            return True

    def __str__(self):
        return self.imie

def walka(malpa, rycerz):
    i=1
    while malpa.czyZywy() and rycerz.czyZywy():
        print('Runda nr:',i)

        if random.randint(0,1) == 0:
            pojedynek(malpa,rycerz)
        else:
            pojedynek(rycerz,malpa)
        wyswietlStaty(malpa, rycerz)
        print("")
        sleep(5)
        i+=1
    if rycerz.czyZywy():
        print('Malpi Wojownik polegl')
        print('Rycerz zwyciezyl walke')
    else:
        print('Rycerz polegl')
        print('Malpi Wojownik zwyciezyla walke')

def pojedynek(x,y):
    print(x,"zostal zaatakowany przez", y)
    obrazenia = y.atak() - x.obrona()
    print(x,'stracil',obrazenia,'punktow zycia')
    x.straconeZycie(obrazenia)

def wyswietlStaty(x,y):
    for i in (x,y):
        if i.zycie <= 0:
            i.zycie = 0
            print(i,'ma',i.zycie,'punktow zycia.')
        else:
            print(i,'ma',i.zycie,'punktow zycia.')

rycerz = Wojownik('Rycerz', random.randint(300,400), random.randint(50,90),random.randint(10,40))
malpa = Wojownik('Malpi Wojownik', random.randint(300,400), random.randint(50,90),random.randint(10,40))

walka(malpa,rycerz)