num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número ({}) es mayor que el segundo número ({})".format(num1, num2))
elif num1 < num2:
    print("El segundo número ({}) es mayor que el primer número ({})".format(num2, num1))
else:
    print("Ambos números son iguales.")