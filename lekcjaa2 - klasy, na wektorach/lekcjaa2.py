#klasa reprezentujaca wektor 2D (x,y)

class Wektor:
    def __init__(self, x = 0.0, y=0.0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)
    #chcemy zeby dzialal +=
    def __isadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Wektor(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Wektor(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Wektor(self.x / other.x, self.y / other.y)

    def wyswietl(self):
        return 'Wspolrzedna x to ' + str(self.x) + ' Wspolrzedna y to ' + str(self.y)
wektor1 = Wektor(6,2)
wektor2 = Wektor(4,8)
wektor3 = wektor1 + wektor2
wektor3 += wektor2
wektor4 = wektor2 * wektor1
print(wektor1.x, wektor1.y)
print('Wektor1:', wektor1.wyswietl())
print(wektor2.x, wektor2.y)
print(wektor2.wyswietl())
print(wektor3.x, wektor3.y)
print(wektor3.wyswietl())
print(wektor4.x, wektor4.y)
print(wektor4.wyswietl())

