from random import randint
los = randint(1,10)
odp = 0
i = 0
print("zgadnij liczbe z przedzialu 1 - 10")
while odp != los:
    odp = int(input("Podaj liczbe: "))
    i+=1
    if odp == los:
        print("Zgadles liczbe! Wylosowana liczba to: ")
        print(odp)
        print("Udało cie się zgadnac liczbe za",i,"proba")
    elif odp > los:
        print("Bledna liczba, wylosowana liczba jest mniejsza od twojej, ponow probe")
    elif odp < los:
        print("Bledna liczba, wylosowana liczba jest wieksza od twojej, ponow probe")
