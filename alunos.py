alunos = ["João", "Maria", "Pedro"]

notas = [
    [7.0, 8.5, 6.0],
    [9.0, 7.5, 9.5],
    [5.5, 6.5, 8.0]
]

for i in range(len(alunos)):
    media = sum(notas[i]) / len(notas[i])
    print(alunos[i], "- Média:", media)