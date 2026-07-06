# Time Complexity:
# - Best: 0(n²)
# - Average: 0(n²)
# - Woert: 0(n²)

# Space Complexity:
# - 0(1)
lista = [7, 4, 2, 9, 1]

for passada in range(len(lista)):
    for i in range(len(lista) - 1 - passada):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)        
