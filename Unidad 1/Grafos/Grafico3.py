import numpy as np
import matplotlib.pyplot as plt

# Función para resolver la ecuación de segundo grado
def resolver_ecuacion_segundo_grado(a, b, c):
    if a <= 0:
        raise ValueError("El coeficiente 'a' debe ser mayor que 0.")
    if 4*a*c <= b**2:
        raise ValueError("Debe cumplirse que 4ac > b^2.")
    
    discriminante = b**2 - 4*a*c
    x1 = (-b + np.sqrt(discriminante)) / (2*a)
    x2 = (-b - np.sqrt(discriminante)) / (2*a)
    
    return x1, x2

# Solicitar datos al usuario
def solicitar_datos_usuario():
    try:
        a = float(input("Ingrese el coeficiente a (mayor que 0): "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        return a, b, c
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return solicitar_datos_usuario()

# Obtener coeficientes del usuario
a, b, c = solicitar_datos_usuario()

# Comprobar y resolver la ecuación
try:
    x1, x2 = resolver_ecuacion_segundo_grado(a, b, c)
    print(f"Las soluciones de la ecuación son x1 = {x1} y x2 = {x2}")
except ValueError as e:
    print(e)

# Crear el rango de valores de x para la gráfica
x = np.linspace(-10, 10, 400)
y = a*x**2 + b*x + c

# Graficar la función cuadrática
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([x1, x2], [0, 0], color='red') # Puntos de las raíces
plt.title('Gráfico de la función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()