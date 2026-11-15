socio = input("Ingrese el nombre de socio: ")
tipo_plan = int(input("Ingrese el tipo de plan: "))
forma_de_pago = input("ingrese la forma de pago: ")
descuento = 0.1


match tipo_plan:
    case 1:
        precio_base = 20000
        if(forma_de_pago == "efectivo"):
            precio_final = precio_base - (precio_base * 0.1)
            print("hay descuento")
        elif(forma_de_pago == "tarjecta"):
            precio_final = precio_base
            print("No hay descuento")
    case 2:
        precio_base = 15000
        if(forma_de_pago == "efectivo"):
            precio_final = precio_base - (precio_base  * 0.1)
            print("hay descuento ")
        elif(forma_de_pago == "tarjecta"):
            precio_final =  precio_base 
            print("No hay descuento ")
    case 3:
        precio_base = 30000
        if (forma_de_pago == "efectivo"):
            precio_final = precio_base - (precio_base * 0.1)
            print("hay descuento en efectivo")
        elif(forma_de_pago == "tarjecta"):
           precio_final = precio_base 
           print("no hay descuento")


    case _:
        print("tipos de plan invalido ")
        plan_valido = False
if plan_valido == True:
    print( socio,"es el nombre del socio","precio final es:", precio_final)
   


            
