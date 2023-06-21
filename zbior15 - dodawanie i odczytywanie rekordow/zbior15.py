def main():
    prac_plik=open("pracownicy.txt","a")
    inny="t"
    print("Podaj dane pracownika: ")
    i=1
    while inny == "t" or inny == "T":
        nazwisko=input("Podaj imie i nazwisko pracownika: ")
        wiek=input("Podaj wiek pracownika: ")
        prac_plik.write(nazwisko + ", " + wiek + "lat\n")
        inny = input("Wybierz 't' jezeli chcesz kontynuowac lub 'p jesli przerwac: ")
        if inny == "p":
            break
        i+=1
    prac_plik.close()
main()
def main2():
    prac_plik=open("pracownicy.txt","r")
    dane=prac_plik.readline()
    while dane != "":
        dane=dane.rstrip("\n")
        print("Imie i nazwisko: ",dane)
        dane=prac_plik.readline()
    prac_plik.close()
main2()