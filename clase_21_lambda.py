from data2 import empleados

def ordenar_emp_genero(e1, e2):
    return e1["gender"] > e2["gender"]
        
def ordenar_emp_nombre(e1, e2):
    return e1["nombre"] > e2["nombre"]
     
def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

 
# empleados.sort(key="gender")

def ordenar_lista(lista, comparador):
    tam = len(lista)
    for i in range (tam - 1):
        for j in range(i + 1, tam):
            if comparador(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                 
# ordenar_lista(empleados, ordenar_emp_genero)

# mostrar_lista(empleados)

#Se puede usar un lambda:
ordenar_lista(empleados, lambda e1, e2 : e1["nombre"] > e2["nombre"])

mostrar_lista(empleados)


# def generar_funciones(calculo):
#     funcion = None
#     if calculo == "sumar":
#         funcion = lambda a, b : a + b
#     elif calculo == "restar":
#         funcion = lambda a, b : a - b
#     elif calculo == "multiplicar":
#         funcion = lambda a, b : a * b
#     elif calculo == "dividir":
#         funcion = lambda a, b : a / b
#     return funcion

# def calcular(a, b, operacion):
#     print(operacion(a,b))

# operacion = input("Ingrese operacion: ")

# calcular(3, 6, generar_funciones(operacion))

