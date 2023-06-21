class Poleprostokata:
    def __init__(self):
        print("Program oblicza pole prostokatu dla bokow a i b")

    def czytajDane(self):
        self.a=float(input("Podaj bok a: "))
        self.b=float(input("Podaj bok b: "))

    def przetworzDane(self):
        self.pole=self.a * self.b
        return self.pole

    def wyswietlDane(self):
        print(f"Pole prostokata o boku a = {self.a}, b = {self.b}, wynosi: {round(self.pole,2)}")

def main():
    pole1=Poleprostokata()
    pole1.czytajDane()
    pole1.przetworzDane()
    pole1.wyswietlDane()
main()