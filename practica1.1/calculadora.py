def calculadora():
    print("Bienvenido a la calculadora")
    print("1 para suma")
    print("2 para resta")
    print("3 para multiplicación")
    print("4 para división")
    print("5 para exponente")
    print("6 para módulo")
    print("7 para salir")

    while True:
        # Pide al usuario que elija una opción
        opcion = input("Elige la operación deseada (1/2/3/4/5/6) o 7 para salir: ")

        # Verifica si el usuario desea salir
        if opcion == "7":
            print("Gracias por visitar mi calculadora, ¡hasta luego!")
            break

        # Verifica si la opción es válida
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Por favor, introduce valores numéricos válidos.")
                continue

            # Realiza la operación correspondiente
            if opcion == "1":
                suma = num1 + num2
                print(f"El resultado de la suma es: {suma}")
            elif opcion == "2":
                resta = num1 - num2
                print(f"El resultado de la resta es: {resta}")
            elif opcion == "3":
                multiplicacion = num1 * num2
                print(f"El resultado de la multiplicación es: {multiplicacion}")
            elif opcion == "4":
                if num2 != 0:
                    division = num1 / num2
                    print(f"El resultado de la división es: {division}")
                else:
                    print("Error: No se puede dividir por cero.")
            elif opcion == "5":
                exponente = num1 ** num2
                print(f"El resultado de la operación exponencial es: {exponente}")
            elif opcion == "6":
                if num2 != 0:
                    modulo = num1 % num2
                    print(f"El resultado del módulo es: {modulo}")
                else:
                    print("Error: No se puede calcular el módulo con divisor cero.")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6 o 7 para salir.")

calculadora()