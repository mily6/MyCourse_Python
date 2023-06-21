import re

wzor = r"banan"
tekst = r"banangruszkabananjablko"


print(re.match(wzor, tekst))

if re.match(r".*" + wzor + r".*", tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.search(wzor, tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

print(re.findall(wzor, tekst))

dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group())
    print(dopasowanie.start())
    print(dopasowanie.end())
    print(dopasowanie.span())

tekst2 = re.sub(wzor, "jagoda", tekst)
print(tekst2)