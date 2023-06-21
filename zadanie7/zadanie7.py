#def czyPalindrom(slowo):
   # lewa_pozycja = 0
    #prawa_pozycja = len(slowo) - 1
    #while prawa_pozycja>=lewa_pozycja:
     #   if slowo[lewa_pozycja] != slowo[prawa_pozycja]:
      #      return False
       # lewa_pozycja+=1
        #prawa_pozycja-=1
    #return True

#slowo=input("Podaj slowo: ")
#print(czyPalindrom(slowo))

#print(len(slowo))
def sprawdz_liste(elementy):
    tymczasowa_wartosc = elementy[0]
    for index in range(len(elementy)):
        if elementy[index]==tymczasowa_wartosc:
            wynik = True
        else:
            wynik = False
            break
    return wynik
print(sprawdz_liste([1,1]))