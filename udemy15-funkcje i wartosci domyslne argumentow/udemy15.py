def BuyME(prefix='Please buy me', what='something nice'):
    print(prefix, what)

BuyME('Please buy me', 'a new car')
BuyME(prefix='Please buy me', what='a car')
BuyME(what='a brand new car', prefix='Please buy me')
BuyME('Please')
BuyME(prefix = 'Please buy me')
BuyME(what='something sweet')

def show_progress(how_many, character='*'):
    line = character * how_many
    print(line)
show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')