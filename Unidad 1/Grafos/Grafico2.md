import matplotlib.pyplot as plt

# Definir los datos a graficar
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Graficar los datos
ax.plot(x, y)

# Agregar título y etiquetas
ax.set_title("Gráfico de la función lineal")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Mostrar la gráfica
plt.show()