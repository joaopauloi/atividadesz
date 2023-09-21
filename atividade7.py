import numpy as np

joaopaulo = np.array([[3, 4, 1], [3, 2, 1]])

soma = 0

for linha in joaopaulo:
    for elemento in linha:
        soma += elemento

print(f"A soma de todos os elementos da matriz é: {soma}")