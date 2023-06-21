liczby=[256,45,98,36,74,86,0,2]

print((len(liczby)))

def sortowanie(liczby):
    for i in range(len(liczby)-1,0,-1):
        for j in range(i):
            if liczby[j]>liczby[j+1]:
                liczby[j], liczby[j+1]=liczby[j+1], liczby[j]
def main():
    print(liczby)
    sortowanie(liczby)
    print("Posortowane liczby: ",liczby)
main()

for m in range(7,0,-1):
    print(m)

