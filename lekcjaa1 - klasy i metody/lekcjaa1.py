class osoba:
    def __init__(self, imie='darek', wiek=30, zarobki=5000):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki

    def przywitanie(self):
        print('Jestem', self.imie, 'i mam', self.wiek, 'lat')

ja = osoba('Adam', 19, 4000)
on = osoba('Erwin', 20, 5000)
tunczyk = osoba()
tunczyk.przywitanie()
ja.przywitanie()
on.przywitanie()
print(tunczyk.imie)
print("")
print(ja.imie)
print(ja.wiek)
print(ja.zarobki)
print("")
print(on.imie)
print(on.wiek)
print(on.zarobki)