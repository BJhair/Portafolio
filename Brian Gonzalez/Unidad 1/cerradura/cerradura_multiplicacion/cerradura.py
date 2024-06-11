print("Cerradura: La multiplicación de dos números reales siempre da como un resultado otro número real.")
print("a * b pertenece R")
print("") #Salto de linea

print("El siguiente programa realiza la propiedad de cerradura")
print("") #Salto de linea

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
multiplicacion = num1 * num2

if multiplicacion.is_integer():
    resultado = "entero"
else:
    resultado = "racional"

print()
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado es un número", resultado)