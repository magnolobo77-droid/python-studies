lista = [10, 5, 3, 7, 20]

procurado = int(input("Número que deseja procurar: "))

encontrou = False

for numero in lista:
    if procurado == numero:
        encontrou = True
        print("Número encontrado", numero)
        break


if encontrou == False:
    print("Número nâo encontrado")


# Forma mais comum em Python:
# if not encontrou:
# É equivalente a:
# if encontrou == False:
        
