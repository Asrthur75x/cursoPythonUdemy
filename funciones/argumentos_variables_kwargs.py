# *args - argumentos - tupla
# **kwargs - keyword arguments (key, value) como un dict

print("** Argumentos variables en forma de Dict **")

def superheroe_superpoderes(nombre, *args, **kwargs):
    print (f"Superheroe: {nombre} - {args} - Mas info: {kwargs}")


#Llamamos la función
superheroe_superpoderes("Spiderman", "Instinto aractino", edad = 17, empresa = "Marvel")
superheroe_superpoderes("Ironman", "Armadura", "Play boy", edad = 45)


#Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", personalidad = "Buena Onda!")