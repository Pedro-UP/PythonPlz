def run():
    contador = 0
    potencia2 = 2**contador
    #Si lo ponemos en mayusculas en vez de ser una variable es una constante
    LIMITE = 1000
    #Mientras que la potencia sea menor a 1000 se repetira el ciclo
    while potencia2 < LIMITE:
        print("2 elevado a la " + str(contador) + " es igual a: " + str(potencia2))
        #Se le coloca el contador mas para tener un conteo del ciclo
        contador = contador + 1
        #Esto es para que se detenga el bucle ya que este ira sumando el valor
        potencia2 = 2**contador


if __name__ == '__main__':
    run()