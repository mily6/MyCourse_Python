import time
import functools
'''
@functools.lru_cache()
def Factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i,Factorial(i)))
stop = time.time()
print('czas:', stop - start)

print(Factorial.cache_info())

'''
'''
start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i,Factorial(i)))
stop = time.time()
print('czas:', stop - start)
'''

@functools.lru_cache(100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result
start = time.time()
for i in range(1,35):
    print('{} - {}'.format(i, fib(i)))
    stop = time.time()
    print('czas:',stop - start)
print(fib.cache_info())