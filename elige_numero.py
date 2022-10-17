# Importamos la libreria random para sacar un numero aleatorio
import random

def run():
    # A la variable le asignaremos un rango aleatorio
    numero_aletorio = random.randrange(1, 100)
    numero_elegido = int(input("Eligue un numero del 1 al 100: "))
    # Mientras que el numero que el usuario escriba sea diferente 
    # al numero aleatorio se repetira lo siguente
    while numero_elegido != numero_aletorio:
        if numero_elegido < numero_aletorio:
            print("Escribe un numero mas grande")
        else:
            print("Escribe un numero mas pequeño")
        numero_elegido = int(input("Eligue otro numero "))
    # Cuando sean los mismos numeros se imprimira esto
    print("***Ganaste Papu***")


if __name__ == '__main__':
    run()