number = 10
print('wartosc:', number, id(number))
number += 2
print('wartosc:', number, id(number))

text='Africa'
print('wartosc:', text, id(text))
text += ' is hot'
print('wartosc:', text, id(text))

list = [1,2,3]
print('Variable list', list, id(list))
list.append(4)
print('Variable list', list, id(list))

list2 = list
print('Variable list2', list2, id(list2))
list2.append(5)
print('Variable list', list, id(list))
print('Variable list2', list2, id(list2))

list3 = list.copy()
print('Variable list', list, id(list))
print('Variable list', list3, id(list3))
print('---------------------------')
days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(days)
print(workdays)