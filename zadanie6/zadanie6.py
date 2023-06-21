import random
liczby=[]
unikalne=[]
for i in range(10):
    liczba = random.randint(0, 10)
    if liczba==0:
        print("Pojawilo sie 0")
        break
    else:
        liczby.append(liczba)
print(liczby)
liczby.sort()
print(liczby)
for j in liczby:
    if j not in unikalne:
        unikalne.append(j)
print(unikalne)
