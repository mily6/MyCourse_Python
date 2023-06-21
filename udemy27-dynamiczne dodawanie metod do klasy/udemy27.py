import csv

brandOnSale = 'Opel'

class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, IsPanitingOK, IsMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPanitingOK = IsPanitingOK
        self.IsMechanicOk = IsMechanicOk
        self.isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.IsPanitingOK and self.IsMechanicOk)

    def GetIsOnSale(self):
        return self.isOnSale

    def SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.isOnSale = newIsOnSaleStatus
            print('Zmieniono status na {} z {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Nie zmieniono statusu, zmiana tylko dla {}'.format(brandOnSale))

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, 'if set to true, the car is available in sale/promo')

car1=Car('Opel', 'Corsa', True, True, True, True)
print(Car.IsDamaged(car1))
print(Car.GetIsOnSale(car1))
print(Car.SetIsOnSale(car1, False))
print(Car.IsOnSale)