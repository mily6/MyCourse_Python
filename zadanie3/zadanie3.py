lista = [4,6,7,2]
print(lista)
lista.sort()
print(lista)

def sortowanie_babelkowe(lista):

    n = len(lista)

    while n  > 1:

        zamien = False
        for l in range():

            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
        n -= 1
        print(lista)
        if zamien == False: break
    return lista
