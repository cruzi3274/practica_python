#DESAFIO FINAL: LA BOLETERA DEL CINE
plan_validar = True
nombre_espectador = input("Ingrese el nombre de espectador: ")
tipo_sala = int(input("Ingrese el tipo de sala de (1 a 3): "))
forma_pago = input("Ingrese la forma de pago: ")

match tipo_sala:
    case 1:
        precio = 4000
    case 2:
        precio = 6000
    case 3:
        precio = 9000
    case _:
        print("tipo de sala invalido ")
        plan_validar = False
if plan_validar == True:
    if forma_pago == "Efectivo":
        precio_final = precio -(precio * 0.2)
        print(nombre_espectador,"el total a adonar es:", precio_final)
    elif forma_pago == "Tarjeta":
        precio_final = precio 
        print(nombre_espectador,"el total a adonar es:", precio_final)
    else:
        print("Forma de pagar invalido: ")