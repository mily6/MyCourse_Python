workDays = [19,21,22,21,20,22]
months = ['I','II','III','IV','V','VI']

monthDays = dict(zip(months, workDays))
print(monthDays)

for key in monthDays:
    print("Key is", key, "value is", monthDays[key])

for value in monthDays.values():
    print('the value is', value)
'''
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
ilosc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_denominations = dict(zip(banknotes_coins, ilosc))

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for i in dict_denominations:
    print('Dominate:', i, '-', 'amount', dict_denominations[i])
'''

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

for d in banknotes_coins:
    dict_denominations[d] = 0
print(dict_denominations)
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for k in sorted(dict_denominations.keys()):
    print("Denominate: {0:6.2f} - amount {1:5}".format(k, dict_denominations[k]))

wiek = [10,20,45,63,24,17,89]
imiona = []

razem = dict(zip(imiona, wiek))
print(razem)
imiona.append("Tomek")
imiona.append("Dawid")
imiona.append("Marcin")
imiona.append("Milosz")
imiona.append("Ola")
imiona.append("Zuzia")
imiona.append("Erwin")
razem = dict(zip(imiona, wiek))

print(razem)
for i in razem.keys():
    print("{} - {}".format(i, razem[i]))
