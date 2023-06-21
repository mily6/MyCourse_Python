def main():
    outfile=open('test.txt','w')
    dane=input("Podaj Imie i nazwisko.\n")
    outfile.write(dane)
    print("Dane zapisano do pliku test.txt")
    outfile.close()
    print()

    infile=open('test.txt','r')
    zawartoscPliku=infile.read()
    print("Dane odczytano z pliku test.txt")
    print(zawartoscPliku)
    infile.close()
main()