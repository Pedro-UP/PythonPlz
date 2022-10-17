def run():
    # Este programa sera para dar solamente los numeros pares
    # for contador in range(20):
    #     # En este caso el contador empesara a realizar el conteo 
    #     # pero solo continuara cuando el numero sea dividido entre dos 
    #     # y no tenga puntos decimales para asi poder sacar los numeros pares
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    for i in range(1000):
        print(i)
        # Break es solo para detener la funcion
        if i == 550:
            break

if __name__ == "__main__":
    run()