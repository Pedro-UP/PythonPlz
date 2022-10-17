#Esto lo estaremos invocando en los tipos de cambio.
#Crearemos 2 parametros los cuales serviran para que cada
#Vez que elijamos el tipo de cambio en esta funcion resiva los
#Parametros que el tipo de cambio tiene
def conversor(tipo_peso, valor_dolar):
    #pesos recibira el parametro tipo de peso es decir
    #la cantidad que coloquemos y devolvera ese valor
    pesos = input("¿Cuantos pesos " +tipo_peso+ " tienes?: ")
    pesos = float(pesos)
    valor_dolar = float(valor_dolar)
    #dolar tomara el valor dolar la cual ya esta definida en cada 
    #tipo de cambio y lo dividira entre el peso para devolver luego el valor
    dolar = pesos/valor_dolar
    dolar = round(dolar, 4)
    dolar = str(dolar)
    print("Tienes $"+ dolar + " dolares")


#Si ponemos triple comilla podemos escribir de la siguiente forma
menu = """
Bienvenido al Conversor de Monedas 

1- Pesos Mexicanos
2- Pesos Argentinos
3- Pesos Colombianos
Elige una Opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Mexicanos", 20.041)
if opcion == 2:
    conversor("Argentinos", 60)
if opcion == 3:
    conversor("Colombianos", 3875)
else:
    print = "Ingrese una Opccion Correcta"


    