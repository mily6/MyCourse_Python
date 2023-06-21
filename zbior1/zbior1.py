from kalkulator import*
def main():
    a=float(input("Podaj a:"))
    b=float(input("Podaj b:"))
    print("Menu")
    print("0 - zakoncz program")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    cyfra=1
    while cyfra != 0:
        cyfra = int(input("Co chcesz wykonac? "))
        if cyfra == 1:
            print("Wynik dodawania:",dodawanie(a,b))
        elif cyfra == 2:
            print("Wynik odejmowania:",odejmowanie(a,b))
        elif cyfra == 3:
            print("Wynik mnozenia:",mnozenie(a,b))
        elif cyfra == 4:
            print("Wynik dzielenia",dzielenie(a,b))
        elif cyfra == 0:
            print("Koniec programu")
        else:
            print("Podales bledna cyfre, sprobuj jeszcze raz")
main()

