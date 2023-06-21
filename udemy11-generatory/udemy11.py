listaA = list(range(6))
listaB = list(range(6))

print(listaA, listaB)

product = []

for i in listaA:
    for j in listaB:
        product.append((i,j))
print(product)
print(len(product))

product = [(i,j) for i in listaA for j in listaB]
print(product)

product = [(i,j) for i in listaA for j in listaB if i % 2 == 1 and j % 2 == 0]
print(product)

product = {i:j for i in listaA for j in listaB if i % 2 == 1 and j % 2 == 0}
print(product)

gen = ((i,j) for i in listaA for j in listaB if i % 2 == 1 and j % 2 == 0)
print(gen)
print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)

gen = ((i,j) for i in listaA for j in listaB if i % 2 == 1 and j % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('Wszystkie wartosci wygenerowano!')
        break
print('--------------------------------------------------------')
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
razem = ((i, j) for i in ports for j in ports)
c=0
print(razem)
for x in razem:
    print(x)
    c+=1
print(c)

razem = ((i, j) for i in ports for j in ports if i!=j)
a=0
for x in razem:
    print(x)
    a+=1
print(a)

razem = ((i, j) for i in ports for j in ports if i<j)
b=0
for (i, j) in razem:
    print("{} - {}".format(i, j))
    b+=1
print(c)
print(a)
print(b)