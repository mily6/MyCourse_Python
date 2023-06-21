lista = [4, 5, 6]

najmniejsza = None
najwieksza = None

for i in lista:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najwieksza == None or najwieksza < i:
        najwieksza = i
print("najmniejsza liczba to: ", najmniejsza)
print("najwieksza liczba to: ", najwieksza)
print("Cala lista: ", lista)