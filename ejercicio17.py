nombre = input("Ingrese su nombre: ")
DD = int(input("Ingrese su dia: "))
MMM = int(input("Ingrese el mes: "))
AAA = int(input("Ingrese el anio: "))

meses = input("ingresar el mes de (enero,febrero,marzo,abril): ")
match meses:
    case "enero":
        print(nombre,"nacio el", DD,  "de", meses, "de", AAA)
    case "febrero" :
        print(nombre,"nacio el", DD, "de", meses, "de", AAA)
    case "marzo":
        print(nombre,"nacio el", DD, "de", meses, "de",AAA)
    case "abril":
        print(nombre,"nacion el",DD, "de", meses, "de", AAA)



