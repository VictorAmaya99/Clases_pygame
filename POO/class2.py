
class Animal:
    def __init__(self, tipo, edad, sonido, tiene_pirulin) -> None:
        self.tipo = tipo
        self.__edad = edad
        self.sonido = sonido
        self.__tiene_pirulin = tiene_pirulin

    #Para validar edad: encapsulamiento
    @property #Convierte a los metodos a una propiedad
    #Funcion disfrazada de variable
    def Edad(self):
        return self.__edad
    
    @Edad.setter
    def Edad(self, value):
        if value > 0:
            self.__edad = value   
    
    @property
    def Sexo(self):
        return "Macho" if self.__tiene_pirulin else "Hembra"
    
    @Sexo.setter
    def Sexo(self, value):
        if value == "Macho" or value == "Hembra":
            self.__tiene_pirulin = True if value == "Macho" else False

    def sonar(self):
        print(self.sonido)


class Mascota(Animal): #para heredar se pone el nombre de la clase padre dentro de los parentesis
    #Metodo constructor
    def __init__(self, tipo, edad, sonido, tiene_pirulin, nombre, vacunado):  #Metodo init sirve para inicializar
                        # da los valores iniciales a la clase
        super().__init__(tipo, edad, sonido, tiene_pirulin) #devuelve la instancia del la clase padre
        self.nombre = nombre
        self.vacunado = vacunado
        #Para ocultar datos al publico        

    #Se pueden agregar mas metodos:
    #Poner self es obligatorio
    def presentarse(self):
        return f"soy una mascota de tipo: {self.tipo}, me llamo {self.nombre}, tengo {self.edad} años y {'Estoy vacunado' if self.vacunado else 'No estoy vacunado'}"
    
    def sonar(self):
        print(f"soy una mascota y hago este sonido {self.sonido}")
    
    def jugar(self):
        print("Estoy jugando")
    
    

   
x = Mascota("Perro", 3, "guauu", True, "Bobby", False)
y = Mascota("Gato", 5, "Miauuu", False, "Colita", True)

z = Animal("cocodrilo", 15, "Siseando", False)

z.sonar()

x.sonar()

# print(x.Edad)
# print(y.Edad)




