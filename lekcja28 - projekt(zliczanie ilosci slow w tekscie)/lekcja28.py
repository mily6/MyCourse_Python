
tekst = input("Podaj tekst: ")
slowa = tekst.split()
print(slowa)
slowo = set(slowa)
print(slowo)
for i in slowo:
    print(f"{i} powtorzylo sie {slowa.count(i)} razy.")