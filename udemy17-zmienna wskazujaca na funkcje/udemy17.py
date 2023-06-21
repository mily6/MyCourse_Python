def BuyMe(what):
    print('Give me', what)

BuyMe('a new car')

StealForMe = BuyMe
print(type(StealForMe))

StealForMe('a new car')

def GoLeft(*args):
    print('PLACEHOLDER - turning left with', *args)
def GoRight(*args):
    print('PLACEHOLDER - turning right with', *args)
def GoForward(*args):
    print('PLACEHOLDER - going forward with', *args)
def GoBack(*args):
    print('PLACEHOLDER - going back with', *args)
def Start(*args):
    print('PLACEHOLDER - starting with', *args)
def Stop(*args):
    print('PLACEHOLDER - stopping with', *args)

instuctions = [Start, GoForward, GoForward, GoLeft, GoForward, GoRight, Stop]

dish = 'pizza'
for instr in instuctions:
    instr(dish)


def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number=8
transformations=[double, square, div2, negative]
tmp_return_value=number

for i in transformations:
    tmp_return_value=i(tmp_return_value)
    print(tmp_return_value)

'''
number = 8
transformations = [double, square, div2, negative]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))
'''