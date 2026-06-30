A = []
B = []
C = []

print("Digite os valores da lista A:")
for i in range(20):
    A.append(float(input(f"A[{i}]: ")))

print("\nDigite os valores da lista B:")
for i in range(20):
    B.append(float(input(f"B[{i}]: ")))

for i in range(20):
    C.append(A[i] - B[i])

print("\nLista C:")
for i in range(20):
    print(f"C[{i}] = {C[i]}")