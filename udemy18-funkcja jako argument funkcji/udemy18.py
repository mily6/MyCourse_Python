def Bake(what):
    print('Baking {}'.format(what))

def Add(what):
    print('Adding {}'.format(what))

def Mix(what):
    print('Mixing {}'.format(what))

cookbook=[(Add, 'milk'), (Add, 'eggs'), (Add, 'flour'), (Add, 'sugar'), (Mix, 'ingredients'),(Bake,'cookies')]

for activity,obj in cookbook:
    activity(obj)

print('-'*30)

def Cook(activity, obj):
    activity(obj)

Cook(Bake, 'brownies')

for activity,obj in cookbook:
    Cook(activity, obj)


def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2
'''
zadanie=[double, square, negative, div2]
liczba=[1,2,3,4,5]

def generate_values(what,liczba):
    wynik=what(liczba)
    print("Dla cyfry", cyfra, 'i funkcji',what.__name__, 'wynik to', wynik)

for what in zadanie:
    for cyfra in liczba:
        generate_values(what, cyfra)
'''
def generate_values(how, x_table):
    value_list = []

    for x in x_table:
        value_list.append(how(x))

    return value_list


x_table = list(range(11))

print('Dla double:', generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))