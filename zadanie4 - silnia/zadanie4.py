def fact(x):
    if x != 0:
        return x * fact(x - 1)
    else:
        return 1
x = int(input("Podaj liczbe: "))
print(fact(x))

