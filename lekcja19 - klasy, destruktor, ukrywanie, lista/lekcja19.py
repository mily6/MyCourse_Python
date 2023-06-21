class Test:
    def __del__(self):
        print("Bye Class")
obj=Test()
obj2=obj
lista=[obj2]
del obj
obj2.__del__()

print("Koniec")

class Test2:
    _lista=[]
    def dodaj(self, arg):
        self._lista.append(arg)
    def zdejmij(self):
        if len(self._lista)>0:
            return self._lista.pop(len(self._lista)-1)
        else:
            return
obj = Test2()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())
obj._lista.append("X")
print(obj._lista)