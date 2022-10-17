#Si ponemos triple comilla podemos escribir de la siguiente forma
menu = """
Bienvenido al Conversor de Monedas 

1- Pesos Mexicanos
2- Pesos Argentinos
3- Pesos Colombianos
Elige una Opcion: """

opcion = int(input(menu))

if opcion == 1:
    # input es por asi decirlo para que el usuario escriba
    pesos = input("¿Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20.041
        # Volvemos a llamar o invocar el valor para que
        # cambie de tipo de dato al que desiemos usar
    valor_dolar = float(valor_dolar)
    dolar = pesos/valor_dolar
        # Se coloca el valor round para definir cuantos decimales puede tener
    dolar = round(dolar, 4)
        # El valor string se escribe solamente str
    dolar = str(dolar)
    print("Tienes $"+ dolar + " dolares")

if opcion == 2:
    # input es por asi decirlo para que el usuario escriba
    pesos = input("¿Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
        # Volvemos a llamar o invocar el valor para que
        # cambie de tipo de dato al que desiemos usar
    valor_dolar = float(valor_dolar)
    dolar = pesos/valor_dolar
        # Se coloca el valor round para definir cuantos decimales puede tener
    dolar = round(dolar, 4)
        # El valor string se escribe solamente str
    dolar = str(dolar)
    print("Tienes $"+ dolar + " dolares")

if opcion == 3:
    # input es por asi decirlo para que el usuario escriba
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
        # Volvemos a llamar o invocar el valor para que
        # cambie de tipo de dato al que desiemos usar
    valor_dolar = float(valor_dolar)
    dolar = pesos/valor_dolar
        # Se coloca el valor round para definir cuantos decimales puede tener
    dolar = round(dolar, 4)
        # El valor string se escribe solamente str
    dolar = str(dolar)
    print("Tienes $"+ dolar + " dolares")

else:
    print = "Ingrese una Opccion Correcta"


    