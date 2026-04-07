print("** Suma con argumentos variables **")

#Función sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total 

#Llamamos a la función sumar 
resultado = sumar (1, 2, 3, 4, 5)
print(f"Resultado de la suma: {resultado}")