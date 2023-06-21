import time

class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)
mem=MemoryClass([])
print("List of items in memory",mem.list_of_items)

mem.list_of_items.append("bla bla")
print("List of items in memory",mem.list_of_items)

mem('buy milk')
print("List of items in memory",mem.list_of_items)


class NoDuplicates:

    def __init__(self):
        self.list = []


    def __call__(self, new_items):
        for a in new_items:
            if not a in self.list:
                self.list.append(a)

my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)

'''
print("Hej klem, jak sie czujesz?")
odp=str(input())
if odp == 'hahaha najedzenina jest okej':
    print("to super, czy moge jakos pomoc?")
    odp5=input()
    if odp5 == 'tak':
        print("super, na co masz ochote? proponuje nalesniki, tosty, albo seks na dachu")
        odp2=input()
        if odp2 == ('nalesniki' or 'tosty'):
            print("oki, juz robie")
            time.sleep(2)
            print("gotowe, smacznego!")
            time.sleep(3)
            print("smakowalo?")
            odp4=input()
            if odp4 == 'tak':
                print("super, milego dnia!")
            else:
                print("Szkoda, nastepnym razem bedzie lepiej, milego dnia!")
        else:
            print("oki mala, zrzucaj wszystko")
            time.sleep(3)
            print('lubudubu bah buh bum bum')
            time.sleep(3)
            print("gicior")
    else:
        print("oki milego dnia!")

else:
    print("przykro mi, na co masz ochote? nalesniki, tosty, zmywanie podlogi czy sex")
    odp3=str(input())
    if odp3 == ('nalesniki' or 'tosty'):
        print("oki, juz sie robi")
    elif odp3 == str('zmywanie podlogi'):
        print('oki tam jest sciera, mopuj!')
    else:
        print('wraar, dawaj dupe')

'''