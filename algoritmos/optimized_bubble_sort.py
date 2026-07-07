"""
Algorithm: Optimized Bubble Sort

Description:
Sorts a list in ascending order using
an optimized Bubble Sort algorithm.
Stops early if no swaps are made.

Time Complexity:
Best Case: 0(n)
Avarage Case: 0(n²)
Worst Case: 0(n²)
"""

lista = [8, 3, 9, 2, 1]

trocou = False

for passada in range(len(lista)):
    trocou = False

    for i in range(len(lista) - 1 - passada):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            trocou = True

    if not trocou:
        break

print(lista)        
        
