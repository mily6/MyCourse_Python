isOk = [0,2,3]
print("Variaable is Ok: ", isOk, type(isOk))
if len(isOk)>3:
    print('True')

options=['load data', 'export data', 'analyze & predict','exit']
def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(int(i+1), options[i]))

choice = 1
#DisplayOptions(options)
while choice:
    DisplayOptions(options)
    #choice = int(input('Select option above or press enter or 0 to exit: '))
    try:
        choice = int(input('Select option above or press enter or 0 to exit: '))
    except ValueError:
        print("Wpisales litere, wpisz cyfre!")
        pass
    if choice == 1:
        print("You choice", options[0])
    elif choice == 2:
        print("You choice", options[1])
    elif choice == 3:
        print("You choice", options[2])
    elif choice == 0:
        print("You choice", options[3])
    else:
        print("Nie ma takiej opcji, ponów próbę!")


'''
opcje = ['load data', 'export data', 'analyze & predict']
print("Opcje do wyboru:")
print("1 - load data")
print("2 - export data")
print("3 - analyze & predict")

for i in range(len(opcje)):
    print("{} - {}".format(int(i + 1), opcje[i]))

wybor = int(input("Którą opcje wybierasz?:"))
if wybor == 1:
    print("Wybrales load data")
elif wybor == 2:
    print("Wybrales export data")
elif wybor == 3:
    print("Wybrales analyze & predict")
else:
    print("Nie ma takiej opcji!")
'''