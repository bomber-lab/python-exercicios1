import random

try:
    qtde = int(input("Digite a quantidade de números (até 50): "))
    if 1 <= qtde <= 50:
        conjunto = set()
        while len(conjunto) < qtde:
            conjunto.add(random.randint(1, 50))
        print(f"Conjunto gerado: {conjunto}")
    else:
        print("Erro: A quantidade deve estar entre 1 e 50.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# Exercício 2
def ler_conjunto(nome):
    entrada = input(f"Digite os números do {nome} separados por espaço: ")
    return set(map(int, entrada.split()))

conjunto1 = ler_conjunto("primeiro conjunto")
conjunto2 = ler_conjunto("segundo conjunto")

print(f"União: {conjunto1 | conjunto2}")
print(f"Interseção: {conjunto1 & conjunto2}")