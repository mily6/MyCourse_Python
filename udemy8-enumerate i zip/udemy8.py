workDays = [19, 21, 22, 21 ,20 ,22]

print(workDays[2])

enumerateDays = list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print('Position', pos, 'value', value)

months = ['I','II','III', 'IV', 'V', 'VI']
print('-----------------------------')
polaczenie=list(zip(months,workDays))
print(polaczenie)

for m, d in polaczenie:
    print('month',m, 'workdays', d)
print('-----------------------------------')
for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'workdays', d)
print('----------------------------------------')
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
projectsANDleaders = list(zip(projects,leaders))
for p, l in projectsANDleaders:
    print("The leader of",p,"is",l)
print("------------------------------------")
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
all=list(zip(projects,dates,leaders))
for p, d, l in all:
    print("The leader of", p,"started", d,"is", l)
'''
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
 
for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))
 
 
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
 
for p, l,d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p,d,l))
 
 
for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))
 
'''