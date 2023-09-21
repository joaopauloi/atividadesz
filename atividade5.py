numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

soma = 0

for numero in numeros:
    soma += numero

print(f"A soma dos números é: {soma}")