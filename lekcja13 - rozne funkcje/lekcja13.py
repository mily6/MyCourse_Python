lista=list(range(10))
print(lista)

nowa=[i*2 for i in lista]
print(nowa)
nowa2=[i+2 for i in lista if i%2==0]
print(nowa2)
argumenty=["Milosz",20]
print("Mam na imie {0}, mam {1} lat. {0}".format(argumenty[0],argumenty[1]))

print(", ".join(["a","b","c"]))
print("Witaj swiecie".replace("Witaj","Czesc"))
print("To jest zdanie.".upper())
print("To jest zdanie.".lower())
print("To jest zdanie.".startswith("To"))
print("To jest zdanie.".endswith("."))
print("jest" in "To jest zdanie")
print("-------------")
lista=[1,3,1]
if all([i%2==0 for i in lista]):
    print("W liscie znajduja sie same liczby parzyste")
if any([i%2==0 for i in lista]):
    print("Przynajmniej jedna liczba parzysta")

for i in enumerate(lista):
    print(i[0]+1,"-",i[1])

