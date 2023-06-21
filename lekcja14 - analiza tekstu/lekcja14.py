plik = open("test.txt","r")
txt=plik.read()
plik.close()
def policz(tekst,znak):
    suma=0
    for i in tekst:
        if i==znak:
            suma+=1
    return suma
litery=(policz(txt.lower(),"p"))
print("Ilosc wystapien podanej litery:", litery)

def main():
    suma=0
    for i in txt:
        if i != " ":
            suma+=1
    return suma
wszystkieLitery=main()
print("Wszystkie litery:",wszystkieLitery)
a=round(litery/wszystkieLitery*100,2)
print(f"litera a stanowi {a}% wszystkich liter")

for z in "abcdefghijklmnoprstuwxyz":
    ile=policz(txt.lower(),z)
    procent=100*ile/wszystkieLitery
    print("{0} - {1} - {2}%".format(z.upper(),ile,round(procent,2)))