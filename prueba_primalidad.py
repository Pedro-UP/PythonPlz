def es_primo(numero):
    contador = 0
        # En el ciclo for le daremos a la variable i el rango de 1 hasta 
        # el numero que nosotros indiquemos tenemos que poner ms 1 porque 
        # siempre cuenta un valor menos
    for i in range(1, numero + 1):
        # Si el valor de i es igual a 1 o el numero que indicamos este 
        # se saltara es decir no contaremos estos valores
        if i == 1 or i == numero:
            continue
        # Si el valor de i no es igual a los numeros de arriba entonces 
        # ejecutaremos esta funcion la cual cada vez que el valor de la 
        # divicion de 0 nos dara el contador +1
        if numero % i == 0:
            contador += 1
    # Si el valor del numero se divide y te da puntos decimal
    if contador == 0:
        return True
    else: 
    # Si el valor que se divide te da 0
        return False

# Aqui solamente pediremos el numero e imprimiremos el resultado
def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es un numero primo")
    else:
        print("No es un numero primo")

if __name__ == '__main__':
    run()