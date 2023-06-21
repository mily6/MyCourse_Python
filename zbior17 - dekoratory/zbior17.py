def duzeLitery(func):
    tekst=func()
    if not isinstance(tekst,str):
        raise TypeError("Podaj ciag znakow")
    return tekst.upper()
def main():
    @duzeLitery
    def wydruk1():
        return "gg"
    print(wydruk1)
main()