# #Entiendo que el def es como si estuviera colocando en una seccion 
# #varias acciones que se guardan en una funcion y luego podemos invocarlas
# def imprmir_funciones():
#     print ("Mensaje especial")
#     print ("Estoy aprendiendo a imprimir funciones")

# imprmir_funciones()
# imprmir_funciones()
# imprmir_funciones()

#Cuando colocamos dentro de una funcion un pareametro en este caso es mensaje
#Es como si estuvieramos diciendo que en ese espacio va a ir la informacion
#Que nosotros coloquemos es decir no se repetira.
def conversacion(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adios")

opcion = int(input("Eligue una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
        conversacion("Elegiste la opcion 2")
elif opcion == 3:
        conversacion("Elegiste la opcion 3")
else:
    print("Escribe la opcion correcta")
