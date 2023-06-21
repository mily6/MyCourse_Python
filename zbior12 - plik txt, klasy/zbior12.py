class Student:
    def zapisujeDaneDoPliku(self):
        outfile=open('test.txt','w')
        self.dane=input("Podaj imie i nazwisko: ")
        outfile.write(self.dane)
        print("Zapisano do pliku")
        print("")

    def odczytujeDaneZPliku(self):
        infile=open('test.txt','r')
        zawartosPliku=infile.read()
        print("Dane odczytano")
        print(zawartosPliku)
        infile.close()
def main():
    obiekt=Student()
    obiekt.zapisujeDaneDoPliku()
    obiekt.odczytujeDaneZPliku()
main()