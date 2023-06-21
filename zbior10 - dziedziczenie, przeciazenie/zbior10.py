import math
class PoleFigury:
    def obliczPole(self):
        print("")
class PoleTrojkata(PoleFigury):
    def obliczPole(self):
        self.a=float(input("Podaj dlugosc podstawy a: "))
        self.h=float(input("Podaj dlugosc wysokosci h: "))
        print("Pole trojkata wynosi:",round(0.5*self.a*self.h,2))
class PoleProstokata(PoleFigury):
    def obliczPole(self):
        self.a=float(input("Podaj dlugosc boku a: "))
        self.b=float(input("Podaj dlugosc boku b: "))
        print("Pole prostokata wynosi:",round(self.a*self.b,2))
class PoleKola(PoleFigury):
    def obliczPole(self):
        self.r=float(input("Podaj dlugosc promienia r: "))
        print("Pole Kola wynosi: ",round(math.pi*self.r**2,2))
class PoleTrapezu(PoleFigury):
    def obliczPole(self):
        self.a=float(input("Podaj dlugosc podstawy a: "))
        self.b=float(input("Podaj dlugosc boku b: "))
        self.h=float(input("Podaj dlugosc wysokosci h: "))
        print("Pole trapezu wynosi:",round(0.5*(self.a+self.b)*self.h,2))
def main():
    wybor = int(input("Menu: 1-trojkata, 2-prostokata, 3-kola, 4-trapezu\nPodaj wybór: "))
    if wybor == 1:
        trojkat=PoleTrojkata()
        trojkat.obliczPole()
    elif wybor == 2:
        prostokat=PoleProstokata()
        prostokat.obliczPole()
    elif wybor == 3:
        kolo=PoleKola()
        kolo.obliczPole()
    elif wybor == 4:
        trapez=PoleTrapezu()
        trapez.obliczPole()
    else:
        print("Zly wybor, ponow probe od 1 do 4")
main()