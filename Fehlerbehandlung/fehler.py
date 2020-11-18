

if __name__ == '__main__':
    while True:
        eingabe = input("Bitte geben sie eine Zahl ein: ")
        try:
            if int(eingabe) % 2 == 0:
                print('Zahl ist gerade')
            else:
                print('Zahl ist ungerade')
            break
        except Exception as e:
            print(f"Fehlermeldung: {e}")
            input("Neuer Versuch [ENTER] oder crtl+c für Abbruch")
            continue
