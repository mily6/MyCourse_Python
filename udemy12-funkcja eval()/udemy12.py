import math

'''
var_x = 10
password = " My super secret password"

source = 'var_x + 3'

#globals = globals().copy()
#del globals['password']
globals={}

result = eval(source, globals)
print(result)
print(source)

#print(globals())
'''
argument_list = []
for i in range(100):
    argument_list.append(i/10)
wzor=input("Wprowadz wzor: ")
for x in argument_list:
    print('{0:3.1f} {1:6.2f}'.format(x,eval(wzor)))


cos=input("Podaj dzialanie:")
tablica = [0,2,4,6,8]
for y in tablica:
    print(y,eval(cos))

