num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
opcion = input("Elegir menu de opciones: ")
print("S - Suma: ")
print("R - Resta: ")
print("M - Multiplicacion: ")
print("D - Division: ")

match ( opcion):
    case 's':
        resultado = num1 + num2
        print(F'El resultado de la suma es = {resultado}')
    case 'r':
        resultado = num1 - num2
        print(F'El resultado de la resta es = {resultado}')
    case 'm':
        resultado = num1 * num2
        print(F'El resutlado de la multiplicacion es = {resultado}')
    case 'd':
        if num2 != 0:
            resultado = float(num1 / num2)
            print(F'El resultado de la division es = {resultado}') 
        else:
            print("Error: no se puede dividir por cero.")

    case _:
        print("Opcion invalido.")
   
        