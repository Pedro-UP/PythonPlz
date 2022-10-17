def run():
    # Este es un diccionario de datos a adiferencia de otros 
    # lenguajes aqui accesamos atravez de llaves en este 
    # podemos acceder atravez de el con cada llave que 
    # nosotros pongamos en vez de acceder atravez del indice.
    # mi_diccionario = {
    #     "llave1" : 1,
    #     "llave2" : 2,
    #     "llave3" : 3,
    # }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    pais_poblacion = {
        "Argentina": 4448555645,
        "España": 6454846611,
        "Mexico": 5855466414,
    }
        # .keys es para tomar lo que esta en cada llave
    # for pais in pais_poblacion.keys():
    #     print(pais)
        # .values es para tomar los valores de cada llave
    # for poblacion in pais_poblacion.values():
    #     print(poblacion)
        # .items es para tomar ambos valores pero tenemos 
        # que especificar en este caso que variables tendran esos valores.
    for pais, poblacion in pais_poblacion.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")

if __name__ == '__main__':
    run()