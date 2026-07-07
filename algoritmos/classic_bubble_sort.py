"""
Algorithm: Classic Bubble Sort
Description:
Sorts a list in ascending order by
repeatedly swapping adjacent elements.

Time Complexity:
Bast Case: 0(n²)
Averange Case: 0(n²)
Worst Case: 0(n²)
"""
lista = [7, 4, 2, 9, 1]

for passada in range(len(lista)):
    for i in range(len(lista) - 1 - passada):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)        
