lista = [ 8, 3, 9, 2, 1]

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
        
