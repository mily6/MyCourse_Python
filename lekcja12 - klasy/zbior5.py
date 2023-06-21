class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    def przedstawSie(self, powitanie = 'Czesc'):
        return powitanie + ", mam na imie " + self.imie + " mam " + str(self.wiek) + " lat"

obiekt = Czlowiek("Sebastian", 24)
print(obiekt.imie, obiekt.wiek)
print(obiekt.przedstawSie("Witam"))
obiekt2 = Czlowiek("Adrian", 20)
obiekt2.imie = "Adrian"
print(obiekt2.przedstawSie())




