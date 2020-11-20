# Parameterübergabe bei Funktionen

def summe(a, b, c=0, d=0):
    print(f"Summe: {a + b + c + d}")


def funktion(a, b, *weitere):
    print("Feste Parameter: ", a, b)
    print("Weitere Parameter: ", weitere)


def funktion2(*args):
    summe = 0
    for a in args:
        summe += a
    print(f"Summe: {summe}")


def funktion3(*args, **kwargs):
    print("Positional: ", args)
    print("Keyword: ", kwargs)


def funktion4(a=None):
    if a:
        print(f"Parameter übergeben: {a}")
    else:
        print("Kein Parameter übergeben")


def funktion5(a: int, b: int) -> str:
    """
    Berechnung Summe aus a und b mit Rückgabe eines Textes mit dem Resultat
    :param a: int
    :param b: int
    :return: str
    """
    summe = a + b
    return f"Summe ist {summe}"


def call(f, **kwargs):
    for arg in kwargs:
        if arg not in f.__annotations__:
            raise TypeError(f"Parameter {arg} unbekannt.")
        if not isinstance(kwargs[arg], f.__annotations__[arg]):
            raise TypeError(f"Parameter {arg} hat ungültigen Typ.")
    ret = f(**kwargs)
    return ret

if __name__ == '__main__':
    summe(2,3,5,6)
    funktion(1, 3, 4, 5, "text")
    funktion2(1, 3, 4, 5)
    funktion3(1, 2, 4, var=10, var1=20)

    # Entpacken von Parameterlisten
    liste_a = (5, 4, 1)
    dict_b = {'a': 5, 'b': 10}
    summe(*liste_a)
    summe(**dict_b)

    # Default Parameter
    funktion4()
    funktion4(10)

    # Anonyme Funktionen
    afunc = lambda x: x * x
    print(f"Resultat Qurdrat: {afunc(3)}")

    # Annotationen
    print(funktion5.__annotations__)
    result = funktion5(2, 5)
    print(result)
    result2 = call(funktion5, a=3, b=3)
    print(result2)
    result3 =call(funktion5, a=3, c=2)
    print(result2)

