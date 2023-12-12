
lista_enteros = [3, 5, 98, 34, 52 , 11, 6]

# def ordenar_enteros(lista, asc = True):
#     tam = len(lista)
#     for i in range(tam - 1):
#         for j in range(i + 1, tam):
#             if asc:
#                 if lista[i] > lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#             else:
#                 if lista[i] < lista[j]: 
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux

# def ordenar_enteros(lista, asc = True):
#     tam = len(lista)
#     for i in range(tam - 1):
#         for j in range(i + 1, tam):
#             if asc and lista[i] > lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#             elif not asc and lista[i] < lista[j]: 
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux

def ordenar_enteros(lista, asc = True):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if asc and lista[i] > lista[j] or not asc and lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
          
print(lista_enteros)

ordenar_enteros(lista_enteros, True)

print(lista_enteros)

ordenar_enteros(lista_enteros, False)

print(lista_enteros)


