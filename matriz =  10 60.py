matriz = [
    [10, 60, 30],
    [80, 20, 55]
]

mascara = [[1 if valor > 50 else 0 for valor in linha] for linha in matriz]

for linha in mascara:
    print(linha)