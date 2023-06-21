print("Podaj dane pracownika")
class Osoba:

    def czytajDane(self):
        self.nazwisko=input("Podaj nazwisko: ")
        self.imie=input("Podaj imie: ")
        self.ulica=input("Podaj ulice: ")

    def wyswietlDane(self):
        print("")
        print("Nazwisko:",self.nazwisko)
        print("Imie:",self.imie)
        print("Ulica:",self.ulica)
class Pracownik(Osoba):
    def czytajDane1(self):
        self.zawod=input("Podaj zawod: ")
    def wyswietlDane1(self):
        print("Zawod:",self.zawod)

def main():
    osoba1=Osoba()
    pracownik1=Pracownik()
    osoba1.czytajDane()
    pracownik1.czytajDane1()
    osoba1.wyswietlDane()
    pracownik1.wyswietlDane1()
main()
