liczby=[1,2,3,4,5,6,7,8,9,10,11]
def suma_zakresu(lista,poczatek,koniec):
    if poczatek>koniec:
        return 0
    else:
        return lista[poczatek]+suma_zakresu(lista,poczatek+1,koniec)
def main():
    print("lista: ",liczby)
    moja_suma=suma_zakresu(liczby,3,5)
    print("Suma podanego zakresu liczb wynosi: ",moja_suma)
main()


