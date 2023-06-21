accounts = {"a": "a"}
while True:
    opcja = input("Wybierz: 'zaloguj sie' lub 'zarejestruj sie'\n")
    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")

    if opcja == "zarejestruj sie":
        accounts[login] = haslo
    elif opcja == "zaloguj sie":
        try:
            accounts[login] == haslo
        except KeyError:
            print("Nie masz konta, zaloz je")
            break
        if accounts[login] == haslo:
            print("Zalogowano sie!")
            break
        elif accounts[login] != haslo:
            print("Bledny login lub haslo, ponow probe")

        elif accounts == {}:
            print("Zaloz konto")
            continue
    else:
        print("Ponow probe, wpisz 'zaloguj sie' lub 'zarejestruj sie' ")

