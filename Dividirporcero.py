while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)   

        break  # Salir del bucle si no hay errores
    except ZeroDivisionError:
        print("¡Error! No se puede dividir entre cero. Intente nuevamente.")