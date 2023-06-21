import random

cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porsche', 'Audi', 'VW', 'Mazda']

def SelectTodayPromotion(list_of_cars):
    a = random.choice(list_of_cars)
    return a

def Delete(a):
    cars.remove(a)

def SelectTodayShow(list_of_cars):
    b = random.choice(list_of_cars)
    return b

def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

p=SelectTodayPromotion(cars)
print("Promotion:", p)
Delete(p)
print(cars)
s=SelectTodayShow(cars)
print("Show:",s)
Delete(s)
print(cars)
print("Free accessories:",SelectFreeAccessories(cars))
