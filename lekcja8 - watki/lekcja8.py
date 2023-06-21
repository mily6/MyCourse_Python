#import random
#from math import pi
#from math import sqrt as pierwiastek

#print(random.randint(1, 10))
#print(pi)
#print(int(pierwiastek(9)))

x = 12
y = 1

try:
    lista = [3]
    print(lista[0])
    print(x + y)
    print(int(x / y))
    print("Linijka po")
#except (ZeroDivisionError, TypeError):
   # print("Wystapil 1 z 2 bledow")
except:
    print("inny blad")
finally:
    print("FINALLY: Wykonam sie i tak")
print("Dalsze instrukcje..")

def dzielenie(x, y):
    assert not y == 0, "Y == 0"
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0")
    print(x / y)

try:
    dzielenie(2, 0)
except ZeroDivisionError:
    print("blad!")
    raise