print("** Funcion par **")

#Función para saber si un numero es par o no 
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
#Llamamos a la función 
#Esta es una condición que solamente se ejecute esta prueba si es que estamos ejecutando el código desde este archivo
#Si el nombre del archivo es igual a main entonces se ejecuta la prueba 
if __name__ == "__main__":
    num = int(input("Proporciona un valor númerico: "))
    print(f"Número par? {es_par(num)}")
