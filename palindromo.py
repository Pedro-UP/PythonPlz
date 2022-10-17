#Aqui definiremos la funcion palindromo esta tendra el parametro palabra
#Dicho parametro ejecutara estas funciones.
def palindromo(palabra):
    #Este es para eliminar el espacio de la frase
    palabra = palabra.replace(" ", "")
    #Aqui vuelve todo en minusculas
    palabra = palabra.lower()
    #Invierte la palabra alrevez y la guarda en una nueva variable
    palabra_invertida = palabra[::-1]
    #Identifica si la palabra que se invirtio es la misma que la original 
    if palabra == palabra_invertida:
        return True
    else:
        False


#Se deja doble salto de linea entre funciones para buenas practicas
#def run es para que se inicie de corrido el programa
def run():
    palabra = input("Escribe una palabra: ")
    #Se invoca por asi decirlo la funcion y se guardara en una nueva variable
    #Esta variable recibe los valores anteriores y realisa la funcion if
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Esta palabra es un palindromo")
    else:
        print("No es un palindromo")


#Aqui se cierra el proceso.
if __name__ == '__main__':
    run()