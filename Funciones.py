#Importacion de libreria
import os

#funciones
def get_full_name(name, last_name):
    full_name = name + ' ' + last_name
    return full_name
print(f"Hola {get_full_name('Ulises', 'Zuniga')}")
os.system('pause')