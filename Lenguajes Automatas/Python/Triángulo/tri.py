import math

def calcular_lado_faltante():
    print("Introduce los valores de dos lados del triángulo rectángulo.")
    print("Deja en blanco el valor del lado que deseas calcular.")
    
    cat1 = input("Cateto 1: ")
    cat2 = input("Cateto 2: ")
    hip = input("Hipotenusa: ")

    #Convertir las entradas a números, si se proporcionan
    cat1 = float(cat1) if cat1 else None
    cat2 = float(cat2) if cat2 else None
    hip = float(hip) if hip else None

    #Calcular el lado faltante usando el teorema de Pitágoras
    if cat1 is None and cat2 is not None and hip is not None:
        cat1 = math.sqrt(hip**2 - cat2**2)
        lado_calculado = "Cateto 1"
    elif cat2 is None and cat1 is not None and hip is not None:
        cat2 = math.sqrt(hip**2 - cat1**2)
        lado_calculado = "Cateto 2"
    elif hip is None and cat1 is not None and cat2 is not None:
        hip = math.sqrt(cat1**2 + cat2**2)
        lado_calculado = "Hipotenusa"
    else:
        return "Error: La calculadora solo funciona si se ingresan dos datos"
    return f"El lado faltante es {lado_calculado} y su valor es: {cat1 if lado_calculado == 'Cateto 1' else cat2 if lado_calculado == 'Cateto 2' else hip:.2f}"

resultado = calcular_lado_faltante()
print(resultado)