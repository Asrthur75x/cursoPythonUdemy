print("** Imprimir detalles de una persona usando kwargs **")

#Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print("\nValores recibidos: ")
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")


#Llamamos a la función
imprimir_detalle_persona(nombre = "Karla", edad = 30, ciudad = "Lima")
imprimir_detalle_persona(nombre = "Pedrito", edad = 50, ciudad = "Moyobamba", puesto = "Gerente")