#UN modulo es un archivo que puede contener la denifición de variables o funciones 

#Definir la función 
def sumar(a, b):
    resultado = a + b
    return resultado


#Prueba de la función sumar 

#Esto es para que se ejecute solo este código en  caso se este ejecutando el código de este archivo. 
if __name__ == '__main__':
    print(f"Prueba función sumar desde el modúlo: {sumar(15, 10)}")