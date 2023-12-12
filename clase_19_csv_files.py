import os

dir_actual = os.getcwd()

#nombre_archivo = input("Ingrese nombre y extension del archivo: ")
path = os.path.join(dir_actual, "personas.csv")

#Procesar el archivo csv y obtener una lista de diccionarios, con la info de las personas del archivo
personas = []

with open(path, "r") as file:
    header = file.readline()
    data = file.readlines()
print(data)

header = header.strip().split(",")
 

for index, item in enumerate(data):
    data[index] = item.strip()

#data = [item.strip() for item in data] #hace lo mismo que el anterior

print(data)

print("----------------------------------------------------------------")

for index, item in enumerate(data):
    data[index] = item.split(",")

print(data) 

for item in data:
    dict_persona = {}
    indice = 0 
    for key in header:
        if item[indice].isdigit():
            item[indice] = int(item[indice])
        dict_persona[key] = item[indice]
        indice += 1
    personas.append(dict_persona)

print("---------------------------------------------------------------")

for persona in personas:
    print(persona)

with open(os.path.join(dir_actual, "personas2.csv"), "w") as file:
    header = ",".join(list(personas[0].keys())) + "\n"

    for persona in personas: 
        values = []
        for value in persona.values():
            if isinstance(value, int):
                value = str(value)
            values.append(value)           
        linea = ",".join(values) + "\n"
        file.write(linea)