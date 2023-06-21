brandOnSale = 'Opel'

class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, IsPanitingOK, IsMechanicOk, IsOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPanitingOK = IsPanitingOK
        self.IsMechanicOk = IsMechanicOk
        self.__IsOnSale = IsOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.IsPanitingOK and self.IsMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -        {}".format(self.isAirBagOk))
        print("Painting  - ok -        {}".format(self.IsPanitingOK))
        print("Air Bag  - ok -        {}".format(self.IsMechanicOk))
        print("IS ON SALE        {}".format(self.__IsOnSale))

    def __GetIsOnSale(self):
        return self.__IsOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__IsOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot Change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')

car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)
car_01.GetInfo()

car_02.__IsOnSale = False
car_02.YearOfProduction = 2005
del car_02.YearOfProduction

setattr(car_02, 'TAXI', False)
delattr(car_02, "TAXI")

car_02.GetInfo()
print(vars(car_02))
car_01.IsOnSale = True
car_02.IsOnSale = True
print("Status of cars:", car_01.IsOnSale, car_02.IsOnSale)

'''
print("Status of cars:", car_01.__GetIsOnSale(), car_02.__GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("Status of cars:", car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.IsOnSale = True
car_02.IsOnSale = True
print("Status of cars:", car_01.IsOnSale, car_02.IsOnSale)
'''