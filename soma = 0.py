soma = 0

for i in range(15):
    numero = int(input(f"Digite o {i + 1}º número: "))

    fatorial = 1
    for j in range(1, numero + 1):
        fatorial *= j

    soma += fatorial

print("Somatório dos fatoriais:", soma)
