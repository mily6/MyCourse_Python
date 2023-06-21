a, b = [2, 5]
print(a)
print(b)

x = 10
y = 20
x, y = y, x
print(x)
print(y)

start, *wszystko, koniec = (1, 2, 3, 4, 5, 6, 7)
print(start)
print(wszystko)
print(koniec)

a = "Parzysta" if 9%2==0 else "Nieparzysta"
print(a)

for i in range(10):
    if i > 5:
        continue
else:
    print("")

try:
    a = 5/0
except ZeroDivisionError:
    print("dzielisz przez zero")
else:
    print("Koniec")
finally:
    print("Zawsze")