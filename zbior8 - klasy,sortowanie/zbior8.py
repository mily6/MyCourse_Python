class Sortowanie:
    def sortujDane(self, liczby):
        for i in range(len(liczby)-1,0,-1):
            for j in range(i):
                if liczby[j]>liczby[j+1]:
                    liczby[j], liczby[j+1]=liczby[j+1], liczby[j]

    def wyswietlWynik(self, liczby):
        print("Posortowane liczby: ",liczby)

def main():
    liczby=[20,45,98,14,3,54]
    obiekt=Sortowanie()
    obiekt.sortujDane(liczby)
    obiekt.wyswietlWynik(liczby)
main()

