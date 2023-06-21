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
'''
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
ports2 = []
for i in ports:
    for j in ports:
        if i != j and i<j:
            ports2.append((i,j))
print(ports2)
'''
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))