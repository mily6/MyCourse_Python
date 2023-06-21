def BuyMe(prefix='Please buy me', what='something nice', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)

BuyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop='market', color='any')

products = ['milk', 'bread', 'flakes']
parameters = {'price':'low', 'time':'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)

def calculate_paint(efficency_Itr_per_m2, *args):
    ilosc=sum(args)
    ilosc_calkowita=efficency_Itr_per_m2*ilosc
    return ilosc_calkowita

print(calculate_paint(2, 2, 10, 16 , 20))

lista=[2,10,16,20]
print(calculate_paint(1, *lista))


def log_it(*args):
    path = r'c:\temp\log_it.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')