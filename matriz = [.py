matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

transposta = []

for coluna in range(len(matriz[0])):
    linha = []
    for linha_original in range(len(matriz)):
        linha.append(matriz[linha_original][coluna])
    transposta.append(linha)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)