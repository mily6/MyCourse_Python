import re

wynik = re.match(r"^((?:He)(?P<first>ll)o) (World)+(!|\.)$", "Hello World!")

if wynik:
    print("Dopasowano")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.group(4))
    print(wynik.groups())
    print(wynik.group("first"))

else:
    print("Nie dopasowano")

if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", "b.a@p.pll"):
    print("Dopasowano")

else:
    print("Nie dopasowano")