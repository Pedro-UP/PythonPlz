contador = 0
print(contador)
while contador < 100:
    contador += 1
    print(contador)

print("Presione tecla para continuar")
input()

#Con for es mucho mas rapido y sencillo ya que al darle un rango
#Este repetira lo que este en el hasta que llegue a la cantidad indicada
#Como conteo toma el primer rango se imprimira hasta que tome el ultimo valor
for conteo in range(1, 101):
    print(conteo)

# conteo = list(range(100))
# print(conteo)
print("Presione tecla para continuar")
input()
print("Tabla del 10")
for i in range(1, 11):
    val = (10*i)
    print("10 * " + str(i) + " = " + str(val))