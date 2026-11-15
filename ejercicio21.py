Nombre_cliente = input("Ingrese el nombre de cliente: ")
Numero_combo = int(input("Ingrese el numero de combo de (1 a 3): "))
Forma_de_pago = input("Ingrese la forma de pago: ")
descuento = 0.15

plan_valido = True
match Numero_combo:
    case 1:
        precio_base = 10000
        
    case 2:
        precio_base = 15000
        
    case 3:
        precio_base = 12000
    case _:
        print(" combo invalido :") 
        plan_valido = False 
    
        

if plan_valido == True:
    if Forma_de_pago == "efectivo":
       precio_final = precio_base - (precio_base * 0.15)
       print(Nombre_cliente,"el total a abonar es:",precio_final)
    elif Forma_de_pago == "tarjeta":
       precio_final = precio_base
       print(Nombre_cliente, "el total a abonar  es:", precio_final)
    else:
        print("Forma de pago invalida")

          