import os  #Hay algunas funciones que da el modulo os, que ayudan a trabajar con los paths
import json
from data import lista

# directorio_actual = os.getcwd() # cwd = current working directory

# print(directorio_actual)

# with open("./archivo.txt", "w") as file:
#     file.write("Hola mundo")

# x = os.path.abspath("./archivo.txt") #Se< usa porque no es bueno trabajar con literales 

# r (raw) = significa que es una cadena cruda para evitar el barra

# print(__file__)

# x = os.path.split(__file__)

# path, nombre = os.path.split(__file__)


# print(path)
# print(nombre)

# path_completo = os.path.join(path, nombre)

# print(path_completo)

###Manera correcta de programar y que funcione en cualquier computadora y cualquiera sistema operativo

# directorio = os.getcwd()
# path_completo = os.path.join(directorio, "pepe.txt ")

# with open(path_completo, "w") as file:
#     file.write("Hola mundo")

directorio = os.getcwd()
path_completo = os.path.join(directorio, "personas.json")

with open(path_completo, "w") as file:
    json.dump(lista, file, indent=4)

