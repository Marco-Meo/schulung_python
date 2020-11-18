# Kommentar

def additionA(value1, value2):
    return value1 + value2

if __name__ == '__main__':
    print("Addition zweier Zahlen")
    v1 = input("Geben sie erste Zahl ein: ")
    v2 = input("Geben sie zweite Zahl ein: ")
    # result = additionA(v1, v2)
    result = additionA(int(v1), int(v2))
    # print("Resultat: %i" % result)
    print(f"Resultat: {result}")