konta = {}
while True:
    opcja = input("'zaloguj sie' lub 'zarejestruj sie': ")
    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")

    if opcja == "zarejestruj sie":
        konta[login] = haslo
        print("Zarejestrowano")
        continue
    if opcja == "zaloguj sie":
        if konta == {}:
            print("Nie masz konta, zarejestruj sie!")
            continue
        elif konta[login] == haslo:
                print("Zalogowano sie!")
                break
        elif konta[login] != haslo:
            print("Podano bledny login lub haslo, ponow probe")
            continue
       # elif konta = {}:
        #    print("Nie masz konta, zarejestruj sie")
         #   continue
    else:
        print("Ponow probe, napisz 'zaloguj sie' lub 'zarejestruj sie'")
