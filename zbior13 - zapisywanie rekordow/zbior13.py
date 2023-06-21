def main():
    liczba_pracownikow=int(input("Podaj liczbe pracownikow: "))
    print("")

    prac_plik=open('pracownicy.txt','w')
    for i in range(liczba_pracownikow):
        dane=input(f"Podaj imie i nazwisko pracownika nr {i+1}: ")
        prac_plik.write(f"nr {i+1}. " + dane + '\n')
    prac_plik.close()
main()
