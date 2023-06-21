for i in range(10):
    print(i)

list = list(range(10))
print('List',list,type(list),id(list))
list2=list[:]
print('List2',list2,type(list2),id(list2))

print(list[-1::-1])

lista=["red", "orange", "green", "violet", "blue", "yellow"]
liczbaN=int(input("Podaj liczbe: "))
def function(lista, liczbaN):
    NowaLista=lista[:]
    return NowaLista[0:liczbaN]
print(function(lista, liczbaN))
print("-----------------------------")
for i in range(1,len(lista)+1):
    print(function(lista,i))

