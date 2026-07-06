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
        
