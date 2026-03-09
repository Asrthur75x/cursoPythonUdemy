print("** FUnción con argumentos por nombre **")

def imprimir_persona(nombre, apellido='', edad=0):
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

#Primero llamamos la funcion pasando los argumentos de manera posicional 
imprimir_persona('Arthur', 'Chapoñan', 22);


#Llamar la función usando argumentos por nombre
imprimir_persona(nombre="Pier", apellido='Chapo', edad=3)


#Llamar la función usando argumentos por nombre, pero intercambiando el orden 
imprimir_persona(edad= 20, nombre='China', apellido='chapi')


#Argumentos con valor por default
imprimir_persona(nombre="Carlos")
imprimir_persona(nombre="Carlos", apellido='Jimenez')