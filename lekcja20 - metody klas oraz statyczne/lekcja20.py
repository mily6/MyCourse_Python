class Czlowiek:
    def __init__(self, imie):
        self.imie=imie
    def przedstaw(self):
        print("Nazywam się " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)
    @staticmethod
    def przywitaj(arg):
        print("Czesc " + arg)

cz1 = Czlowiek.nowy_czlowiek("Sebastian")
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek("Dominik")
cz2.przedstaw()
obiekt=Czlowiek("Milosz")
obiekt.imie="Dawid"
print(obiekt.imie)
obiekt.przedstaw()
Czlowiek.przywitaj("przyjacielu")
