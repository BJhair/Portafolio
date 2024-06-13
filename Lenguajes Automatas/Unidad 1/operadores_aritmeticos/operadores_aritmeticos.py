print("Se ingresan dos números en el programa y este hará las operaciones de suma, resta, multiplicación y división")
print()
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("La suma de {} más {} es {}".format(num1, num2, suma))
print("La resta de {} menos {} es {}".format(num1, num2, resta))
print("La multiplicación de {} por {} es {}".format(num1, num2, multiplicacion))
print("La división de {} entre {} es {}".format(num1, num2, division))