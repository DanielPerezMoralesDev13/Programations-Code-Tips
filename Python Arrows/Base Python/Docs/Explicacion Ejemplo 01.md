<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion Ejemplo 01***

```python
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

if __name__ == "__main__":
    """
    Las funciones lambda en Python pueden ser de una línea solamente, no permiten múltiples líneas.
    """
    # Ejemplo de uso: Aplicar una función lambda que duplica el número 15.
    print(apply(number=15, f=lambda num: 2 * num), end="\n")
```

---

## ***Conceptos Clave***

1. **Funciones Lambda:** *En Python, las funciones lambda son funciones anónimas de una sola línea.*

2. **Sintaxis Compacta:** *Las funciones lambda permiten una sintaxis más compacta y pueden ser útiles cuando la función es simple y no requiere múltiples líneas de código.*

---

### ***Características***

- **Limitaciones:** *Las funciones lambda en Python están restringidas a una única expresión y no permiten múltiples líneas de código.*

---

### ***Ejemplo Práctico***

```python
if __name__ == "__main__":
    # Ejemplo de uso: Aplicar una función lambda que duplica el número 15.
    print(apply(number=15, f=lambda num: 2 * num), end="\n")
```

- *Este ejemplo muestra cómo utilizar una función lambda de una línea como argumento de la función `apply` en Python, aplicando la operación de duplicar el número 15 de manera concisa y directa.*
