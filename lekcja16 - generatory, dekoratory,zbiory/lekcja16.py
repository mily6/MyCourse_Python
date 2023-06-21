def gen():
    i = 0
    while i < 5:
        yield i
        i+=1

for i in gen():
    print(i)
print(list(gen()))

def parzyste(x):
    i=0
    while i <= x:
        if i%2==0:
            yield i
        i+=1
for i in parzyste(6):
    print(i)

def decorator(func):
    def wrapper():
        print("-------")
        func()
        print("-------")
    return wrapper
def hello():
    print("Hello world")
hello2 = decorator(hello)
hello2()

print()

@decorator
def witaj():
    print("Witaj swiecie")
witaj()


liczby1={0,1,2,4,4}
slowa=set(["a","b","c"])

print(liczby1)
print(slowa)

liczby1.add(5)
print(liczby1)

liczby1.remove(0)
print(liczby1)
liczby1.add(3)
print(liczby1)

print(1 in liczby1)
liczby1={0,1,2,4,4}
liczby2={3,4,5,6}
print(liczby1 | liczby2)
print(liczby1 & liczby2)
print(liczby1 - liczby2)
print(liczby2 ^ liczby1)
