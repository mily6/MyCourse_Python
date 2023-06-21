dayType = 3

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)

price = 123
bonus = 23
bonus_granted = True
price = price - bonus if bonus_granted else price
print(price)

rating = 5

something = 'very good' if rating == 5 else 'good' if rating == 4 else 'weak'
print(something)