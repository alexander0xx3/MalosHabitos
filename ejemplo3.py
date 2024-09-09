
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto



def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura



def main():

    opcion = input("¿Qué área desea calcular? Ingrese '1' para rectángulo o '2' para triángulo: ")

    if opcion == '1':

        ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
        alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
        print("Área del rectángulo:", area_rectangulo)

    elif opcion == '2':

        base_triangulo = float(input("Ingrese la base del triángulo: "))
        altura_triangulo = float(input("Ingrese la altura del triángulo: "))
        area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print("Área del triángulo:", area_triangulo)

    else:
        print("Opción no válida. Por favor, elija '1' o '2'.")



if __name__ == "__main__":
    main()
