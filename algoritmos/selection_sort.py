"""
Algorithm: Selection Sort

Description:
Sorts a list in ascending order by
selecting the amallest
element from the unsorted portion of the list and swapping
it with the first unsorted element.

Time Complexity:
Best Case: 0(n²)
Average Case: 0(n²)
Worst Case: 0(n²)

Space Complexity:
0(1)
"""
lista = [6, 3, 8, 1]

for i in range(len(lista)):
               menor = i
               for j in range(i + 1, len(lista)):
                   if lista[j] < lista[menor]:
                       menor = j
                       lista[i], lista[menor] = lista[menor], lista[i]

print(lista)               
               
