lista_adresow = []

def dodaj_adres():
    imie = input("Dodaj dane: ")
    lista_adresow.append(imie)
    print("Podaj kolejna opcje")
def kasuj_adres():
    print("Kasuj dane")
    index=int(input("Który adres usunac?: "))
    lista_adresow.remove(lista_adresow[index-1])
    print("Podaj kolejna opcje")

def wyswietl_dane():
    print("Wyswietl Dane")
    for index in range(len(lista_adresow)):
        print(f'{index + 1}: {lista_adresow[index]}')
    print("Podaj kolejna opcje")

opcja=1
print("Menu: ")
print("1 - Dodaj imie i nazwisko")
print("2 - Kasuj imie i nazwisko")
print("3 - Wyswietl Dane")
print("0 - Koniec programu")
while opcja != 0:
    opcja = int(input("Wybierz opcje: "))
    if opcja == 1:
        dodaj_adres()
    elif opcja == 2:
        kasuj_adres()
    elif opcja == 3:
        wyswietl_dane()
    elif opcja == 0:
        print("Koniec programu")
        print("Twoja lista:\n",lista_adresow)
    else:
        print("Bledna opcja, ponow probe")