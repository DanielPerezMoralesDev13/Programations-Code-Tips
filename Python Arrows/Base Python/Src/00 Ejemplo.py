#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable

def apply(number: int | float, f: Callable) -> int | float:
    """
    Aplica una función dada a un número y devuelve el resultado.

    Args:
        number (int | float): El número al que se aplicará la función.
        f (Callable): La función que se aplicará al número.

    Returns:
        int | float: El resultado de aplicar la función al número.
    """
    return f(number)

def double(number: int | float) -> int | float:
    """
    Duplica un número.

    Args:
        number (int | float): El número a duplicar.

    Returns:
        int | float: El número duplicado.
    """
    return 2 * number

if __name__ == "__main__":
    # Ejemplo de uso: Aplicar la función double al número 15.
    print(apply(number=15, f=double))
