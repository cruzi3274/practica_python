dia_num = int(input("Ingrese el dia de semana de (1 a 7):"))

match dia_num:
    case 1:
        print("El numero", dia_num, "corresponde al dia lunes: ")
    case 2:
        print("El numero", dia_num, "corresponde al dia martes: ")
    case 3:
        print("El numero", dia_num, "corresponde al dia miercules: ") 
    case 4:
        print("El numero", dia_num, "corresponde al dia jueves: ")
    case 5:
        print("El numero", dia_num, "corresponde al dia viernes: ")
    case 6:
        print("El numero", dia_num, "corresponde al dia sabado: ")
    case 7:
        print("El numero", dia_num, "corresponde al dia domingo: ")
    case _:
        print("Los dia de semana invalido")
        
    