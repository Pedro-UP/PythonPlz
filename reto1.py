def run():
    texto = "Esto es un texto"
    contador = 0
    while contador < 10:
        contador += 1
        if contador == 5:
            break
        print(contador, texto)

if __name__ == '__main__':
    run()