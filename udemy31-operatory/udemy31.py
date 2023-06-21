'''
class Car:


    def __init__(self, brand, model, isAirBagOk, IsPanitingOK, IsMechanicOk, accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPanitingOK = IsPanitingOK
        self.IsMechanicOk = IsMechanicOk
        self.accessories = accessories
    def IsDamaged(self):
        return not (self.isAirBagOk and self.IsPanitingOK and self.IsMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -        {}".format(self.isAirBagOk))
        print("Painting  - ok -        {}".format(self.IsPanitingOK))
        print("Air Bag  - ok -        {}".format(self.IsMechanicOk))
        print("Accessories            {}".format(self.accessories))

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return  Car(self.brand, self.model, self.isAirBagOk, self.IsPanitingOK, self.IsMechanicOk, accessories)

        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.IsPanitingOK, self.IsMechanicOk, accessories)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return (self, other)
        else:
            raise Exception ("Adding type {} to Car is not implemented".format(type(other)))

    def __str__(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model)

car_01 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
car_02 = Car('Opel', 'Corsa', True, False, True, True)
car_01+=(['rims', 'navigation system'])
car_01.GetInfo()
car_02.GetInfo()
print(car_01.IsDamaged())

car_01 += 'loudspeeker system'
car_01.GetInfo()

carp_pack = car_01 + car_02
print('car_01+car_02=',carp_pack[0].brand, carp_pack[1].brand)

print(car_01)
'''


class Cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)


    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __iadd__(self, other):
        if type(other) is list:
            additives=self.additives
            additives.extend(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        elif type(other) is str:
            additives = self.additives
            additives.append(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        else:
            raise Exception ('Bledna zmienna {}'.format(type(other)))
    def __str__(self):
        return 'name: {}, kind: {}, additives: {}'.format(self.name, self.kind, self.additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)
cake01 += ['strawberry', 'cherry'], 5
print(cake01)
