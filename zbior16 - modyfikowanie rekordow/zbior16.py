import os


def main():
    znaleziony=False
    plik=open("pracownicy.txt","r")
    temp_file=open("temp.txt","w")
    szukaj=input("Podaj imie i nazwisko ktore chcesz zmodyfikowac: ")
    nowe_dane=input("Podaj nowe dane pracownika: ")
    dane=plik.readline()
    while dane!="":
        wiek=plik.readline()

        dane=dane.rstrip("\n")
        wiek=wiek.rstrip("\n")

        if szukaj==dane:
            temp_file.write(nowe_dane + "\n")
            temp_file.write(wiek + "\n")
            znaleziony=True
        else:
            temp_file.write(dane + "\n")
            temp_file.write(wiek + "\n")
        dane=plik.readline()
    plik.close()
    temp_file.close()

    os.remove("pracownicy.txt")
    os.rename("temp.txt","pracownicy.txt")

    if znaleziony:
        print("Plik zostal uaktulniony")
    else:
        print("szukane imie i nazwisko nie zostalo znalezione")
    plik=open("pracownicy.txt","r")
    dane=plik.readline()
main()

