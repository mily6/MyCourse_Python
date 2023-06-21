car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibiza',
'carIsAirBagOK' : True,
'carIsPanitingOK' : True,
'carIsMechanicOk' : True
}

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPanitingOK' : False,
'carIsMechanicOk' : True
}
def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPanitingOK'] and aCar['carIsMechanicOk'])

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))
cars=[car_01, car_02]
for i in cars:
    print("{} {} Is Damaged?: {}".format(i['carBrand'], i['carModel'],IsCarDamaged(i)))

cake_01 = {
'taste' : 'vanilia',
'glaze' : 'chocolade',
'cake_text' : 'Happy Brithday',
'cake_weight' : 0.7
}
cake_02 = {
'taste' : 'tee',
'glaze' : 'lemon',
'cake_text' : 'Happy Python Coding',
'cake_weight' : 1.3
}

def show_cake_info(aCake):
    return (aCake['taste'],aCake['glaze'],aCake['cake_text'],aCake['cake_weight'])
cakes=[cake_01,cake_02]

for i in cakes:
    print('taste - {}, glaze - {}, cake_text - {}, cake_weight - {}'.format(i['taste'],i['glaze'],i['cake_text'],i['cake_weight'],show_cake_info(i)))
