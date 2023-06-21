slownik = {1: "Poniedzialek", 2: "Wtorek", 7: "Niedziela"}
slownik2={}
slownik2["login"]="haslo"
print(slownik2)

print(slownik[7])
slownik[3]="Sroda"
slownik[4]= False
slownik[5]=5
print(slownik)

print("\nPętla")
for l in slownik.values():
    print(l)
print("-----")
print(slownik.pop(1))
print(slownik)

krotka=(2,4,8,16,32,64,128)
print(krotka[0])

print("Elementow:", krotka.count(2))
print("Index:", krotka.index(64))

print("\nWycinki:")
print(krotka[0:10])
print(krotka[-4:-2])
print(krotka[0:7:2])
print(krotka[:4:-1])
print(krotka[::-1])
