import random
class Tablica1:
    def zapelnijTablice(self,N,tablica):
        for i in range(N):
            for j in range(N):
                liczba=random.randint(1,9)
                if i==j:
                    tablica[i][j]=liczba
                else:
                    tablica[i][j]=0
        for i in range(N):
            for j in range(N):
                print(tablica[i][j]," ",end="")
            print()

    def obliczSume(self,N,tablica):
        suma=0
        for i in range(N):
            suma+=tablica[i][i]
        print("Suma liczb na przekatnej = ",suma)
def main():
    N=10
    tablica=[[0 for i in range(N)] for j in range(N)]
    obiekt=Tablica1()
    obiekt.zapelnijTablice(N,tablica)
    obiekt.obliczSume(N,tablica)
main()