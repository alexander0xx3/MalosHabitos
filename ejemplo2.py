def calcular_producto_y_suma(factor1, factor2, suma):
    resultado = factor1 * factor2 + suma
    return resultado


def ejecutar_calculo():
    # Entrada de valores
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    suma_adicional = float(input("Introduce el valor a sumar: "))

    resultado_final = calcular_producto_y_suma(numero1, numero2, suma_adicional)
    print("El resultado es:", resultado_final)


ejecutar_calculo()