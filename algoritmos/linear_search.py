"""
Algorithim: Linear Search

Description:
Seaches for a value in a list by
cheking each element sequentially

Time Complexity:
Best case: 0(1)
Avarage Case: 0(n)
Worst Case: 0(n)
"""

lista = [10, 5, 3, 7, 20]

procurado = int(input("Número que deseja procurar: "))

encontrou = False

for numero in lista:
    if procurado == numero:
        encontrou = True
        print("Número encontrado", numero)
        break


if encontrou == False:
    print("Número não encontrado")


# More Pythonic way (recommend):
# if not encontrou:
# is equivalent to:
# if encontrou == False:
        
