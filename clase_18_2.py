from data import lista

def ordenar_personas(lista, atributo = str, asc = True):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if asc and lista[i][atributo] > lista[j][atributo] or not asc and lista[i][atributo] < lista[j][atributo]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def mostrar_persona(persona):
    print(f"{persona['id']}, {persona['nombre']}, {persona['edad']}, {persona['gender']}, {persona['sector']}")

#ordenar por genero y dentro del genero por nombre
#cuando tengo dos personas me fijo el genero
#si son de distinto genero ---> me fijo si estan desordenadas por genero y de ser necesario las swap
#si son del mismo genero (dos mujeres o dos varones)----> me fijo si estan desordenados por nombre
#se ordenan primero las mujeres y despues los varones
#y dentro del mismo genero alfabeticamente por nombre

def mostrar_personas(lista):
    print(" Lista   de    Personas ")
    print("Id    Nombre     Edad      Genero    Sector")
    for persona in lista:
        mostrar_persona(persona)
        

mostrar_personas(lista)

# tam = len(lista)
# for i in range(tam - 1):
#     for j in range(i + 1, tam):
#         if lista[i]['sector'] > lista[j]['sector']:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
        # if lista[i]['gender'] > lista[j]['gender']:
        #     aux = lista[i]
        #     lista[i] = lista[j]
        #     lista[j] = aux
        # elif lista[i]['gender'] == lista[j]['gender']:
        #     if lista[i]['nombre'] > lista[j]['nombre']:
        #         aux = lista[i]
        #         lista[i] = lista[j]
        #         lista[j] = aux

tam = len(lista)
for i in range(tam - 1):
    for j in range(i + 1, tam):
        if lista[i]['sector'] > lista[j]['sector']:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        elif lista[i]['sector'] == lista[j]['sector']:
            if lista[i]['gender'] > lista[j]['gender']:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            elif lista[i]['gender'] == lista[j]['gender']:
                if lista[i]['nombre'] > lista[j]['nombre']:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

mostrar_personas(lista)