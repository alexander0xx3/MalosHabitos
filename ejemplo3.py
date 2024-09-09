# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura


# Función principal
def main():
    # Solicitar al usuario qué cálculo desea realizar
    opcion = input("¿Qué área desea calcular? Ingrese '1' para rectángulo o '2' para triángulo: ")

    if opcion == '1':
        # Solicitar datos para el rectángulo
        ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
        alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
        print("Área del rectángulo:", area_rectangulo)

    elif opcion == '2':
        # Solicitar datos para el triángulo
        base_triangulo = float(input("Ingrese la base del triángulo: "))
        altura_triangulo = float(input("Ingrese la altura del triángulo: "))
        area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print("Área del triángulo:", area_triangulo)

    else:
        print("Opción no válida. Por favor, elija '1' o '2'.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
