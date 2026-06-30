import random

qtde = int(input("Digite a quantidade de números: "))

lista = [random.randint(1, 100) for _ in range(qtde)]
print(f"Lista original: {lista}")

lista_sem_repetidos = list(dict.fromkeys(lista))

print(f"Lista sem repetidos: {lista_sem_repetidos}")
print(f"Tamanho da nova lista: {len(lista_sem_repetidos)}")