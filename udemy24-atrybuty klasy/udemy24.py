class Car:

    def __init__(self, brand, model, isAirBagOk, IsPanitingOK, IsMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPanitingOK = IsPanitingOK
        self.IsMechanicOk = IsMechanicOk

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.IsPanitingOK, car_01.IsMechanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.IsPanitingOK, car_02.IsMechanicOk)


class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

cake01 = Cake('Vanilla Cake', 'Cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery_offer=[]
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

print("Today in our offer: ")
for i in bakery_offer:
    print(i.name, '-', '(',i.kind,')', 'main taste:', i.taste, 'with additives of', i.additives, 'filled with', i.filling)
    print()
'''
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
'''