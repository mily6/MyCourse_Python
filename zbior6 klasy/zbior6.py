import math


class Trojmian:
    def __init__(self):
        print("Program obliczajacy pierwiastki rownania")
    def podaj(self):
        self.a=int(input("Podaj a: "))
        if self.a==0:
            print("'a' musi byc rozne od 0")
            exit()
        else:
            self.b = int(input("Podaj b: "))
            self.c = int(input("Podaj c: "))
            self.delta=self.b**2-4*self.a*self.c
            if self.delta<0:
                print(f"Brak pierwiastkow rownania")

            else:
                self.x1=round((-self.b-math.sqrt(self.delta))/(2*self.a),2)
                self.x2=round((-self.b+math.sqrt(self.delta))/(2*self.a),2)

    def wyswietl(self):
        if self.delta>0:
            print(f"Dwa pierwiastki, x1 = {self.x1}, x2 = {self.x2}")
        elif self.delta==0:
            print(f"Pierwiastek podwojny x1 = {self.x1}")

def main():
    obiekt=Trojmian()
    obiekt.podaj()
    obiekt.wyswietl()
main()