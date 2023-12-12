import os
import json

def mostrar_persona(persona):
    print(f"{persona['id']}, {persona['nombre']}, {persona['edad']}, {persona['gender']}, {persona['sector']}")


def mostrar_personas(lista):
    print(" Lista   de    Personas ")
    print("Id    Nombre     Edad      Genero    Sector")
    for persona in lista:
        mostrar_persona(persona)

directorio = os.getcwd()
path_completo = os.path.join(directorio, "personas.json")

with open(path_completo, "r") as file:
    data = json.load(file)


mostrar_personas(data)