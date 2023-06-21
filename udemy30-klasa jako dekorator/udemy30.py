
import random
'''
class MemoryClass:

    list_of_already_selected_items = []

    def __init__(self, funct):
        print('>> this is init of MemoryClass')
        self.funct=funct

    def __call__(self, list):
        print('<< this is call of MemoryClass instance')
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print('+-- selecting only from a list of', items_not_selected)
        item = self.funct(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        return item
cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porsche', 'Audi', 'VW', 'Mazda']

@MemoryClass
def SelectTodayPromotion(list_of_cars):
    a = random.choice(list_of_cars)
    return a

@MemoryClass
def SelectTodayShow(list_of_cars):
    b = random.choice(list_of_cars)
    return b

@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

print("Promotion:", SelectTodayPromotion(cars))

print("Show:",SelectTodayShow(cars))

print("Free accessories:",SelectFreeAccessories(cars))

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

    def add_additives(self, additives):
        self.additives.extend(additives)

class NoDuplicates:
    def __init__(self, funct):
        self.funct=funct

    def __call__(self, cake, additives):
        no_duplicate_list=[]
        for i in additives:
            if i not in cake.additives:
                no_duplicate_list.append(i)
        self.funct(cake, no_duplicate_list)

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts', 'jez'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()
add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts', 'makambe', 'jez'])
cake01.show_info()
'''
def Konstruktor(funkcja):
    def Wrapper():
        print('-------')
        funkcja()
        print('-------')
    return Wrapper

def World():
   print('Hello World')

World2=Konstruktor(World)
World2()

print('*****************')

@Konstruktor
def Witaj():
    print('Witaj')

Witaj()
print('************')
Witaj2=Witaj
Witaj2()

World()
'''