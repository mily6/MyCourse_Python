myvar = 'Hello'
myvar2 = myvar+'!!'
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Ta sama wartosc?', myvar == myvar2)
print('Ta sama wartosc?', myvar is myvar2)
print(id(myvar), id(myvar2))
myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Ta sama wartosc?', myvar == myvar2)
print('Ta sama wartosc?', myvar is myvar2)
print(id(myvar), id(myvar2))