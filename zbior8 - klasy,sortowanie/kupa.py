liczby=[2,8,6,3]
n=len(liczby)
for i in range(n-1,0,-1):
    print(liczby)
    for j in range(i):
        if liczby[j]>liczby[j+1]:
            liczby[j], liczby[j+1]=liczby[j+1], liczby[j]
print(liczby)