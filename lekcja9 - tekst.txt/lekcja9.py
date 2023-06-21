plik = open("test.txt", "a")
if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n")
plik.close()

plik = open("test.txt", "r")

#if plik.readable():
 #   print("Zawartosc pliku: ")
  #  tekst = plik.readlines()
   # print(tekst)
    #for l in tekst:
     #   print(l)
    #tekst = plik.read()
    #print(tekst)
if plik.readable():
     print("Zawartosc pliku: ")
     for l in plik:
            print(l)