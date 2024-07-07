#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from typing import List

# Lista de precios que son considerados caros
expensive: List[int] = [32, 20]

# Suma de los elementos en la lista 'expensive'
total_sum: int = sum(expensive)

# Imprime la suma total de los elementos en la lista
print(total_sum, end = "\n")  # Esto imprimirá: 52
