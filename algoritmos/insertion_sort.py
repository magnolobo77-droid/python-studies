"""
Algorithm: Insertion Sort

Description:
Sorts a list in asceding order by
inserting each element
from the unsorted portion into its
correct position
in the sorted portion of the list.

Time Complexity:
Best Case: 0(n)
Averange Case: 0(n²)
Worst Case: 0(n²)

Space Complexity:
0(1)
"""
numeros = [7, 4, 6, 2, 9]

for i in range(1, len(numeros)):
    chave = numeros[i]
    j = i - 1


    while j >= 0 and numeros[j] >= chave:
        numeros[j + 1] = numeros[j]
        j = j - 1
    

    numeros[j + 1] = chave

print(numeros)    
        
