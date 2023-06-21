def main():
    prac_plik=open("pracownicy.txt","r")
    dane=prac_plik.readline()
    while dane != "":
        dane=dane.rstrip("\n")
        print("Imie i nazwisko: ",dane)
        dane=prac_plik.readline()
    prac_plik.close()
main()
