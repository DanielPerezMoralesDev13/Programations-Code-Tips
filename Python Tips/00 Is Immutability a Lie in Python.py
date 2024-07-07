
def primerEjemplo() -> str:
    text: str = "hello"
    text = text + "!"
    return text

def segundoEjemplo() -> str:
    coordinates: tuple[float, float] = (1, 2)
    coordinates += 3
    # Dara error -> TypeError: can only concatenate tuple (not "int") to tuple
    print(coordinates)


def tercerEjemplo() -> str:
    coordinates: tuple[float, float] = (1, 2)
    print("Before:", id(coordinates))

    # Dara error no se puede modificar el valor de un indice en una tabla
    # TypeError: 'tuple' object does not support item assignment
    # coordinates[0] = 10

    # Solucion ponerle una coma al final
    coordinates += 3,
    print("After:", id(coordinates))
    
    # No dara error
    print(coordinates)

def cuartoEjemplo() -> str:
    text: str = "hello"
    text[0] = "H"
    # TypeError: 'str' object does not support item assignment
    return text

if __name__ == "__main__":
    cuartoEjemplo()