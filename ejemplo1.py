def fmultiplicacion(factor1, factor2):
    producto = factor1 * factor2
    return producto
if __name__=="__main__":
    multiplicando = float(input("multiplicnado: "))
    multiplicador = float(input("multiplicador: "))

    resultado = fmultiplicacion(multiplicando, multiplicador)
    print(f" {multiplicando} * {multiplicador} = {resultado}")