import re

if re.match("^[Rr]ok[=_-][0-9][0-9][0-9][0-9]$", "rok-1995"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

print("")

if re.match("^[A-Z][a-z]*$","Ala"):
    print("Dopasowano")
else:
    print("Niedopasowano")

print("")

if re.match("^[A-Z][a-z]+$","Aza"):
    print("Dopasowano")
else:
    print("Niedopasowano")

print("")

if re.match("^[A-Z][a-z]?[A-Z]$","AA"):
    print("Dopasowano")
else:
    print("Niedopasowano")

print("")

if re.match("^[A-Z][a-z]{2,5}$","AnIa"):
    print("Dopasowano")
else:
    print("Niedopasowano")