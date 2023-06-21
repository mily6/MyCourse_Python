class Car:

    def __init__(self, brand, model, isAirBagOk, IsPanitingOK, IsMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPanitingOK = IsPanitingOK
        self.IsMechanicOk = IsMechanicOk

    def IsDamaged(self):
        return not (self.isAirBagOk and self.IsPanitingOK and self.IsMechanicOk)

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_01.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.IsPanitingOK, car_01.IsMechanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.IsPanitingOK, car_02.IsMechanicOk)


class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Taste: {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))

    def set_filling(self,filling):
        self.filling=filling

    def add_additives(self, additives):
        self.additives.extend(additives)

cake01 = Cake('Vanilla Cake', 'Cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

cake02.set_filling('vanilla cream')
cake03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer:")
for c in bakery_offer:
    c.show_info()
    print()