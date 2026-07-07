"""
Algorithm: Binary Search

Description:
Searches for a value in a sorted list
using the divide-and-conquer strategy.

Requeriment:
The list must be sorted.

Time Complexity:
Bast Case: 0(1)
Avarege Case: 0(log n)
Worst Case: 0(log n)
"""

# Ordered list to perform binary search
lista = [2, 4, 6, 8, 10, 12, 14, 16]

procurado = int(input("Digite um número que deseja procurar: "))

# Search limits
inicio = 0
fim = len(lista) - 1
encontrado = False

while inicio <= fim:
    # Calculate the middle element of the current range
    meio = (inicio + fim) // 2

    if lista[meio] < procurado:
                inicio = meio + 1
                
    elif lista[meio] > procurado:
                fim = meio - 1
                
    else:
        print("Número encontrado", procurado)
        
        encontrado = True
        break


if not encontrado:
    print("Número não encontrado")

            
